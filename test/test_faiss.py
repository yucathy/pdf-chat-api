# test/test_faiss.py
from app.pdf_utils import extract_chunks_from_pdf
from app.embed_utils import get_embeddings_for_chunks, get_embedding
from app.vector_store import VectorStore

# Step 1: Get chunks
chunks = extract_chunks_from_pdf("app/can_ai_solve_crime.pdf")

# Step 2: Get embeddings
embeddings = get_embeddings_for_chunks(chunks)

# Step 3: Build FAISS index
store = VectorStore(dim=1536)
store.add(embeddings, chunks)

# Step 4: Query something
query = "What is this document about?"  # try change it
query_vector = get_embedding(query)
results = store.search(query_vector)

# Show results
for i, (text, score) in enumerate(results):
    print(f"\nResult {i+1} (distance: {score:.4f}):\n{text}")
