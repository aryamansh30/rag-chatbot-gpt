import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from vectors import retriever
from dotenv import load_dotenv
load_dotenv()

# LLM and prompt setup (reuse from main.py)
model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=st.secrets["OPENAI_API_KEY"])

template = """
You are an expert in answering questions about different APIs provided to you. Answer as specifically and accurately as possible.
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

# Streamlit UI
st.set_page_config(page_title="RAG API Chatbot", page_icon="🤖")
st.title("🔗 API RAG Chatbot")
st.write("Ask me anything about public APIs! (Data from your CSV)")

if "history" not in st.session_state:
    st.session_state.history = []

question = st.text_input("Ask your question:", key="input")

if st.button("Submit") or (question and st.session_state.get("last_question") != question):
    if question.strip():
        context_docs = retriever.invoke(question)
        context = format_context(context_docs)
        result = chain.invoke({"context": context, "question": question})
        #st.session_state.history.append({"question": question, "answer": result})
        st.session_state.history.append({"question": question, "answer": result.content})
        st.session_state.last_question = question

# Display chat history
for chat in reversed(st.session_state.history):
    #st.markdown(f"**You:** {chat['question']}")
    #st.markdown(f"**Bot:** {chat['answer']}")
    st.markdown(f"**Bot:** {chat['answer']}")

st.markdown("---")
st.markdown("Made with [Streamlit](https://streamlit.io/) and [LangChain](https://www.langchain.com/)")
