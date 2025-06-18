# app/test_embed.py
from pdf_utils import extract_chunks_from_pdf
from embed_utils import get_embeddings_for_chunks

chunks = extract_chunks_from_pdf("app/can_ai_solve_crime.pdf")
embeddings = get_embeddings_for_chunks(chunks)

print(f"Total chunks: {len(chunks)}")
print(f"Total embeddings: {len(embeddings)}")

for i, emb in enumerate(embeddings[:3]):
    print(f"\n--- Embedding {i+1} ---")
    print(f"Length: {len(emb)}")
    print(f"Preview (first 5 dims): {emb[:5]}")
