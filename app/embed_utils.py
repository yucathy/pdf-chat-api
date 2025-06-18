# app/embed_utils.py
import os
from openai import OpenAI
from typing import List


# Load API key from environment
print(os.environ.get("OPENAI_API_KEY"))
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def get_embedding(text: str, model: str = "text-embedding-ada-002") -> List[float]:
    """Generate a single embedding vector for one text string"""
    response = client.embeddings.create(
        input=[text],
        model=model
    )
    return response.data[0].embedding

def get_embeddings_for_chunks(chunks: List[str], model: str = "text-embedding-ada-002") -> List[List[float]]:
    """Generate embeddings for a list of text chunks"""
    return [get_embedding(chunk, model) for chunk in chunks]
