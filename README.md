# LangSmith Masterclass

A hands-on project exploring **LangChain, LangGraph, and LangSmith** with practical examples of LLM applications, agents, RAG pipelines, tracing, evaluation, and observability.

## Topics Covered

- LangChain fundamentals
- LLM chains and prompts
- Tool calling and agents
- RAG and vector stores
- LangGraph workflows
- LangSmith tracing and observability
- Monitoring and evaluation
- Dataset creation and annotation
- User feedback
- Agent workflows

## LangSmith

The project demonstrates how LangSmith can be used for:

- **Observability** — inspect individual traces, prompts, model calls, tools, latency, tokens, and errors.
- **Monitoring & Alerting** — track application health across multiple runs.
- **Evaluation** — measure and compare LLM application quality.
- **Dataset Creation & Annotation** — create reusable datasets for testing and evaluation.
- **User Feedback** — associate user feedback with production traces.
- **Collaboration** — share traces, datasets, and evaluations with a team.

## Setup

```bash
git clone <repository-url>
cd langsmith

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

Create a .env file:
```bash
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=your_project_name

OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
```

Running Examples:
```bash
python tracables/4_agent.py
```