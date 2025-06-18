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

### 3. Build and run the app with Docker Compose
```bash
docker-compose up --build
```
Then open http://localhost:8000

---

## ⛏️ Project Structure
```bash
pdf-chat-api/
├── app/
│   ├── main.py           # FastAPI app entry point
│   ├── pdf_utils.py      # PDF processing functions (text extraction, chunking)
│   ├── embed_utils.py    # OpenAI embedding helpers
│   ├── vector_store.py   # FAISS indexing and searching
│   └── chat.py           # GPT answer generation logic
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env
```

---

## Future Work

- Add UI with Streamlit or Gradio
- Add multi-PDF support
- Add persistent storage (e.g., PostgreSQL + Supabase)
- Add authentication (JWT)
- Improve text chunking logic with sentence-level splitting (e.g., using NLTK or spaCy)
- Switch from L2 to cosine similarity for better semantic matching

