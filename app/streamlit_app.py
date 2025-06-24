# streamlit_app.py
import streamlit as st
import requests
import os


st.set_page_config(page_title="PDF Chatbot", layout="centered")

st.title("📄💬 Chat with your PDF")

API_URL = os.getenv("API_URL", os.environ.get("API_URL"))

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
question = st.text_input("Ask a question about this document")

if uploaded_file and question:
    with st.spinner("Sending to FastAPI..."):
        # Save uploaded file
        with open("app/tmp.pdf", "wb") as f:
            f.write(uploaded_file.read())

        payload = {
            "question": question,
            "pdf_path": "app/tmp.pdf"  # this path is readable while using fastAPI 
        }

        try:
            res = requests.post(API_URL, json=payload)
            res.raise_for_status()
            data = res.json()
            st.markdown("### 🤖 GPT Answer")
            st.write(data["answer"])

            with st.expander("🔍 Top Matching Chunks"):
                for i, chunk in enumerate(data["top_chunks"], 1):
                    st.markdown(f"**Chunk {i}:**\n```\n{chunk}\n```")

        except requests.exceptions.RequestException as e:
            st.error(f"API Error: {e}")

