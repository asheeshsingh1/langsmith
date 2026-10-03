## RAG Failures
RAG apps have two big failure modes:
1. Retriever errors - wrong / irrelevant docs retrieved.
2. Generator errors - model hallucinates or misuses context.

In production, it's often unclear where the failure happened. Was the retriever bad, or did the LLM ignore the docs?

LangSmith automatically records:
* User query
* Retrieved documents
* LLM prompt (with inserted docs)
* LLM response