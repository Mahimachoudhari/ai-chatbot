from langchain_community.llms import Ollama

llm = Ollama(model="mistral")

def generate_answer(context, query):
    prompt = f"""
You are a ChatGPT-like AI assistant.

Context:
{context}

Question:
{query}

Give a proper, helpful answer.
"""

    response = llm.invoke(prompt)

    return response