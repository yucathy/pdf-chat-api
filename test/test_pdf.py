# test/test_pdf.py
from app.pdf_utils import extract_chunks_from_pdf

chunks = extract_chunks_from_pdf("app/can_ai_solve_crime.pdf")

for i, chunk in enumerate(chunks):
    print(f"--- Chunk {i+1} ---")
    print(chunk)
    print()