from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template='Capital city of {country}',
    input_variables=['country']
)

prompt2 = PromptTemplate(
    template='Leanguage spoken by most people in this city {city}',
    input_variables=['city']
)

model1 = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
model2 = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

parser = StrOutputParser()

chain = prompt1 | model1 | parser | prompt2 | model2 | parser

config = {
    "run_name":"Sequential Chain",
    "metadata":{
        "model1":"gemini-3.5-flash",
        "model2":"gemini-3.6-flash"
    },
    "tags":["sequential llm","learning"]
}

result = chain.invoke({'country': 'India'},config=config)

print(result)