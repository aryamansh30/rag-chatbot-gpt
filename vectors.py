from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

df = pd.read_csv("public_apis_clean.csv")
embeddings = OpenAIEmbeddings()

documents = []
for i, row in df.iterrows():
    document = Document(
        page_content=row["category"] + " " + row["description"],
        metadata={
            "API key": row["api"],
            "auth": row["auth"],
            "HTTPS": row["https"],
            "cors": row["cors"],
            "link": row["link"],
            "description": row["description"]
        },
        id=str(i)
    )
    documents.append(document)

vector_store = FAISS.from_documents(documents, embeddings)
retriever = vector_store.as_retriever(search_kwargs={"k": 5})