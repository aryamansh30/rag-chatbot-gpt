from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from vectors import retriever
from dotenv import load_dotenv
load_dotenv()

#model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=st.secrets["OPENAI_API_KEY"])
import os
model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=os.environ["OPENAI_API_KEY"])

template = """
You are an exeprt in answering questions about different APIs provided to you. Answer as specifically and accurately as possible.
You have to ensure you are giving the correct output and also ensure you are formatting it well.

Here are the API keys: {context}

Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def format_context(docs):
    formatted = []
    for doc in docs:
        meta = doc.metadata
        link = meta.get('link', '')
        api_name = meta.get('API key', '')
        formatted.append(
            f"API: {api_name}\n"
            f"Description: {meta.get('description', '')}\n"
            f"Auth: {meta.get('auth', '')}\n"
            f"HTTPS: {meta.get('HTTPS', '')}\n"
            f"CORS: {meta.get('cors', '')}\n"
            f"Endpoint: {link}"
        )
    return "\n---\n".join(formatted)

while True:
    print("\n\n-------------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n\n")
    if question == "q":
        break
    
    context_docs = retriever.invoke(question)
    context = format_context(context_docs)
    result = chain.invoke({"context": context, "question": question})
    print(result)