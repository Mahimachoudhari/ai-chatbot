from langchain_community.llms import Ollama

llm = Ollama(model="mistral")

def generate_answer(query, vector_store):

    docs = vector_store.similarity_search(query)

    context = "\n".join([d.page_content for d in docs])

    return llm.invoke(f"""
    Context:
    {context}

    Question:
    {query}
    """)