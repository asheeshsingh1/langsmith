from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_classic.agents import create_react_agent, AgentExecutor
from langsmith import Client
from dotenv import load_dotenv

import requests
import os


load_dotenv()

os.environ["LANGSMITH_PROJECT"] = "Agent Workflow"


search_tool = DuckDuckGoSearchRun()


@tool
def get_weather_data(city: str) -> str:
    """
    This function fetches the current weather data for a given city.
    """
    url = (
        "https://api.weatherstack.com/current"
        f"?access_key=YOUR_KEY"
        f"&query={city}"
    )

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    return str(data)


llm = ChatOpenAI()


# Pull ReAct prompt from LangSmith
client = Client()

prompt = client.pull_prompt(
    "hwchase17/react",
    dangerously_pull_public_prompt=True,
)


# Create ReAct agent
agent = create_react_agent(
    llm=llm,
    tools=[search_tool, get_weather_data],
    prompt=prompt,
)


# Wrap agent with executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool, get_weather_data],
    verbose=True,
    max_iterations=5,
)


response = agent_executor.invoke(
    {"input": "What is the current temp of Gurgaon using get weather data"}
)

print(response)
print(response["output"])