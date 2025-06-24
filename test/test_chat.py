# test/test_chat.py
from app.pdf_utils import extract_chunks_from_pdf
from app.embed_utils import get_embeddings_for_chunks, get_embedding
from app.vector_store import VectorStore
from app.chat import ask_gpt

# Step 1: Load and chunk PDF
chunks = extract_chunks_from_pdf("app/can_ai_solve_crime.pdf")

# Step 2: Embed all chunks
embeddings = get_embeddings_for_chunks(chunks)

# Step 3: Build FAISS index
store = VectorStore(dim=1536)
store.add(embeddings, chunks)

# Step 4: Ask a question
question = "What is this document mainly about?"
query_vector = get_embedding(question)
top_chunks = [text for text, _ in store.search(query_vector, k=3)]

# Step 5: Send to GPT
response = ask_gpt(question, top_chunks)

print("\n✅ GPT Answer:")
print(response)
