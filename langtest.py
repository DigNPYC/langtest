from langchain_openai import ChatOpenAI

llm = ChatOpenAI(openai_api_key="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")

llm.invoke("how can langsmith help with testing?")