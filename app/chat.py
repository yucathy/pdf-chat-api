# app/chat.py
import os
from openai import OpenAI
from typing import List

from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def build_prompt(question: str, context_chunks: List[str]) -> str:
    """Combine question and retrieved chunks into a single prompt"""
    context = "\n\n".join(context_chunks)
    return f"""You are a helpful assistant.

Answer the following question using only the information from the context below.

Context:
{context}

Question:
{question}

Answer:"""

def ask_gpt(question: str, context_chunks: List[str], model: str = "gpt-3.5-turbo") -> str:
    """Send the combined prompt to OpenAI's chat completion API"""
    prompt = build_prompt(question, context_chunks)

    response = client.responses.create(
        model=model,
        input=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.output_text
