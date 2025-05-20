# RAG API Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that answers questions about public APIs using a CSV knowledge base, LangChain, OpenAI, and Streamlit.

## About the Project

This project is a chatbot that leverages Retrieval-Augmented Generation (RAG) to answer user questions about public APIs. It uses a CSV file as its knowledge base, retrieves relevant API information using vector search (FAISS), and generates accurate, context-aware answers using OpenAI's GPT-3.5-turbo model. The chatbot can be run both as a command-line interface (CLI) and as a web app via Streamlit.
Link for streamlit application: https://rag-chatbot-gpt.streamlit.app/


## Setup Instructions

### 1. **Clone the Repository**
```sh
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### 2. **Create and Activate a Virtual Environment**
```sh
python3 -m venv .venv
source .venv/bin/activate
```

### 3. **Install Dependencies**
```sh
pip install -r requirements.txt
```

### 4. **Set Up Your OpenAI API Key**

#### For Local Development:
- Create a `.env` file in the project root:
  ```
  OPENAI_API_KEY=sk-...
  ```

#### For Streamlit Cloud:
- Go to your app’s settings on [Streamlit Cloud](https://share.streamlit.io/).
- Add your OpenAI API key in the **Secrets** section:
  ```
  OPENAI_API_KEY = "sk-..."
  ```

### 5. **Run the Chatbot**

#### Command-Line Interface:
```sh
python main.py
```

#### Streamlit Web App:
```sh
streamlit run app.py
```
- Open the provided local URL in your browser.



## Project Structure & File Descriptions

| File/Folder                | Purpose                                                                                  |
|---------------------------|------------------------------------------------------------------------------------------|
| `app.py`                  | Streamlit web app for interactive chatbot experience.                                    |
| `main.py`                 | Command-line interface for the chatbot.                                                  |
| `vectors.py`              | Loads the CSV, builds the vector store, and exposes the retriever for RAG.               |
| `public_apis_clean.csv`   | The knowledge base: a CSV file containing public API details.                            |
| `requirements.txt`        | Python dependencies for the project.                                                     |
| `.env`                    | (Not committed) Stores your OpenAI API key for local development.                        |
| `.streamlit/secrets.toml` | (Not committed) Stores your OpenAI API key for Streamlit Cloud deployment.               |
| `.gitignore`              | Ensures secrets and unnecessary files are not committed to git.                          |


## About Each File

### `app.py`
- The main Streamlit app.
- Loads the retriever and LLM, formats context, and provides a chat interface.
- Reads the OpenAI API key from Streamlit secrets.

### `main.py`
- CLI version of the chatbot.
- Reads the OpenAI API key from the environment (via `.env`).
- Useful for quick local testing.

### `vectors.py`
- Loads the CSV knowledge base.
- Creates document embeddings using OpenAI.
- Builds a FAISS vector store for fast similarity search.
- Exposes a `retriever` object for use in both CLI and web app.

### `public_apis_clean.csv`
- The knowledge base for the chatbot.
- Contains details about various public APIs (name, description, auth, HTTPS, CORS, link, etc.).

### `requirements.txt`
- Lists all Python dependencies required for the project.

### `.env`
- **Not committed to git.**
- Stores your OpenAI API key for local development.

### `.streamlit/secrets.toml`
- **Not committed to git.**
- Stores your OpenAI API key for Streamlit Cloud deployment.

### `.gitignore`
- Ensures that sensitive files (like `.env` and `.streamlit/secrets.toml`) and unnecessary files are not tracked by git.


## Notes

- The chatbot uses FAISS for in-memory vector search, which works on both local and Streamlit Cloud deployments.
- You can expand the knowledge base by adding more rows to `public_apis_clean.csv`.

## Citations

- Use of LLMs
  - ChatGPT for creating embeddings and computing the API keys
  - Gemini for creating comprehensive README with appropriate formatting 

**Enjoy your RAG-powered API chatbot!**
