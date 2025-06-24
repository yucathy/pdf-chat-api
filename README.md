# 📄 PDF Chat API

A lightweight backend service that allows users to upload a PDF file and ask questions about its content.  
Built with **FastAPI**, **OpenAI Embeddings**, and **FAISS**, this app supports semantic search over documents and integrates with GPT to answer user questions based on retrieved chunks.

---

## 🚀 Features

- 📄 Upload and parse PDF files into clean text chunks
- 🧠 Convert text into embeddings using OpenAI's embedding API
- 🔍 Store and search vectors with FAISS (vector database)
- 🤖 Use GPT (ChatCompletion API) to answer questions about the PDF content
- 🐳 Fully containerized with Docker
- 🔐 Secure with environment variable support via `.env`

---

## 🛠️ Tech Stack

- **FastAPI** – modern async Python API framework  
- **Uvicorn** – ASGI server for serving FastAPI  
- **OpenAI API** – for both embeddings and GPT chat  
- **FAISS** – for vector similarity search  
- **PyMuPDF** – for PDF text extraction  
- **Docker & docker-compose** – for environment isolation and easy deployment

---

## 📦 Getting Started

### 1. Clone this repository

```bash
git clone git@github.com:your-username/pdf-chat-api.git
cd pdf-chat-api
```

### 2. Set your OpenAI API Key and create a .env file
```bash
OPENAI_API_KEY=your-api-key-here
```

### 3. Build and run the app and show the UI with Docker Compose
```bash
docker-compose up --build
```
Then open http://localhost:8000
And
http://localhost:8051 (UI to upload pdf using stramlit)

### 4. Run test file
```bash
docker-compose exec api python -m test.test_xxxx
```

### 5. Check the database
```bash
sqlite3 app/query_history.db
SELECT * FROM query_log;
```

---

## ⛏️ Project Structure
```bash
pdf-chat-api/
├── app/
│   ├── streamlit_app.py  # Streamlit UI
│   ├── main.py           # FastAPI app entry point
│   ├── routes.py         # FastAPI logit point
│   ├── pdf_utils.py      # PDF processing functions (text extraction, chunking)
│   ├── embed_utils.py    # OpenAI embedding helpers
│   ├── vector_store.py   # FAISS indexing and searching
│   ├── query_log.py      # Store query log
│   └── chat.py           # GPT answer generation logic
├── test/
│   ├── test_embed.py    
│   ├── test_faiss.py   
│   ├── test_chat.py
│   └── test_pdf.py           
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── test_ask.sh           # test chatbot function using curl
└── .env
```

---

## Future Work
🧠 1. Semantic Search Optimization
- Replace L2 distance with cosine similarity to improve high-dimensional vector retrieval accuracy
- Experiment with different chunking strategies (fixed-length, sentence-based, or automatic segmentation)
- Introduce keyword filtering to increase semantic relevance between retrieved chunks and queries
- Design and conduct quantitative evaluations using test sets to measure chunk relevance coverage
🤖 2. Response Quality & Prompt Engineering
- Refine the prompt to instruct GPT to only answer based on retrieved chunks
🚀 3. Performance & Cost Optimization
- Implement embedding caching and persistence to avoid redundant vectorization
- Design a response-level caching mechanism using query hashes to store previously answered results
- Track and optimize query response time and OpenAI token usage
- Benchmark performance between storage methods (e.g., SQLite vs. Pickle vs. vector DB)
🌍 4. Multilingual and Advanced Feature Support
- Add support for multilingual PDF documents, including Chinese (e.g., jieba segmentation)
- Integrate with external vector databases such as Milvus, Qdrant, or Chroma for scalable knowledge retrieval
- Enable multi-document indexing and querying
- Provide UI enhancements like chunk-level highlighting and expandable references
🧪 5. Enhanced Demo & Deployment Experience
- Support deployment to Render, Hugging Face Spaces, or AWS EC2
- Provide a screen-recorded demo video or interactive notebook for presentation
- Implement CI/CD workflows for format checking, unit testing, and auto-deployments
- Add persistent storage (e.g., PostgreSQL + Supabase)
- Add authentication (JWT)
