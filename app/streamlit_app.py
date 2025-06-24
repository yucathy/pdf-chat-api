# streamlit_app.py
import streamlit as st
from pdf_utils import extract_chunks_from_pdf
from embed_utils import get_embeddings_for_chunks, get_embedding
from vector_store import VectorStore
from chat import ask_gpt
from query_log import log_query

st.set_page_config(page_title="PDF Chatbot", layout="centered")

st.title("📄💬 Chat with your PDF")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
question = st.text_input("Ask a question about this document")

if uploaded_file and question:
    with st.spinner("Reading and processing..."):
        # Save uploaded file
        with open("app/tmp.pdf", "wb") as f:
            f.write(uploaded_file.read())

        # Extract + embed + build index
        chunks = extract_chunks_from_pdf("app/tmp.pdf")
        embeddings = get_embeddings_for_chunks(chunks)
        store = VectorStore(dim=1536)
        store.add(embeddings, chunks)

        # Question → embedding → search → GPT
        query_vector = get_embedding(question)
        top_chunks = [text for text, _ in store.search(query_vector, k=3)]
        answer = ask_gpt(question, top_chunks)

        # Log result
        log_query(question, answer, "app/tmp.pdf")

        st.markdown("### 🤖 GPT Answer")
        st.write(answer)

        with st.expander("🔍 Context used"):
            for i, chunk in enumerate(top_chunks, 1):
                st.markdown(f"**Chunk {i}**:\n```\n{chunk}\n```")
