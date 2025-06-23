# app/routes.py
from fastapi import APIRouter, Request
from pydantic import BaseModel
from .pdf_utils import extract_chunks_from_pdf
from .embed_utils import get_embeddings_for_chunks, get_embedding
from .vector_store import VectorStore
from .chat import ask_gpt
from .query_log import log_query

router = APIRouter()

class AskRequest(BaseModel):
    question: str
    pdf_path: str  # For now, just provide path to existing sample PDF

@router.post("/ask")
def ask_route(payload: AskRequest):
    # Load and process document
    chunks = extract_chunks_from_pdf(payload.pdf_path)
    embeddings = get_embeddings_for_chunks(chunks)

    # Build FAISS index
    store = VectorStore(dim=1536)
    store.add(embeddings, chunks)

    # Embed question & search
    query_vector = get_embedding(payload.question)
    top_chunks = [text for text, _ in store.search(query_vector, k=3)]

    # Generate answer
    answer = ask_gpt(payload.question, top_chunks)
    log_query(payload.question, answer, payload.pdf_path)
    return {
        "question": payload.question,
        "answer": answer,
        "top_chunks": top_chunks
    }
