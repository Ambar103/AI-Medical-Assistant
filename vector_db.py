import faiss
import numpy as np
from embeddings import get_embedding

class VectorDB:
    def __init__(self, texts):
        self.texts = texts
        self.embeddings = get_embedding(texts)

        dim = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(np.array(self.embeddings))

    def search(self, query, k=3):
        query_vec = get_embedding([query])
        distances, indices = self.index.search(np.array(query_vec), k)
        return [self.texts[i] for i in indices[0]]