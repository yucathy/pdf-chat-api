# app/vector_store.py
import faiss
import numpy as np
from typing import List, Tuple

class VectorStore:
    def __init__(self, dim: int = 1536):
        self.index = faiss.IndexFlatL2(dim)  # L2 distance
        self.vectors = []  # list of np.array
        self.text_chunks = []

    def add(self, vectors: List[List[float]], texts: List[str]):
        """Add vectors + corresponding texts to the index"""
        np_vectors = np.array(vectors).astype("float32")
        self.index.add(np_vectors)
        self.vectors.extend(np_vectors)
        self.text_chunks.extend(texts)

    def search(self, query_vector: List[float], k: int = 3) -> List[Tuple[str, float]]:
        """Return top-k most similar text chunks with their distances"""
        query_np = np.array([query_vector]).astype("float32")
        distances, indices = self.index.search(query_np, k)
        results = []
        for i, dist in zip(indices[0], distances[0]):
            if i < len(self.text_chunks):
                results.append((self.text_chunks[i], dist))
        return results
