# app/pdf_utils.py
import fitz  # PyMuPDF
from typing import List

def extract_text_from_pdf(file_path: str) -> str:
    """Extract full text content from a PDF file"""
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def chunk_text(text: str, max_chars: int = 500) -> List[str]:
    """
    Split text into chunks of max_chars length.
    Keeps paragraphs together when possible.
    """
    paragraphs = text.split("\n")
    chunks = []
    current_chunk = ""

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        if len(current_chunk) + len(para) <= max_chars:
            current_chunk += " " + para
        else:
            chunks.append(current_chunk.strip())
            current_chunk = para
    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def extract_chunks_from_pdf(file_path: str, max_chars: int = 500) -> List[str]:
    """
    High-level function to extract and chunk text from a PDF file.
    """
    full_text = extract_text_from_pdf(file_path)
    return chunk_text(full_text, max_chars=max_chars)
