from endee import Endee, Precision
from embeddings import get_embedding

class EndeeVectorDB:
    def __init__(self):
        self.client = Endee()

       
        self.client.set_base_url("http://localhost:8080/api/v1")

        self.index_name = "medical_index"

        try:
            self.client.create_index(
                name=self.index_name,
                dimension=384,
                space_type="cosine",
                precision=Precision.INT8
            )
            print("Index created")
        except Exception as e:
            print("Index already exists")

        self.index = self.client.get_index(self.index_name)

        self.data_loaded = False

    def add_data(self, texts):
        if self.data_loaded:
            return

        embeddings = get_embedding(texts)

        data = []
        for i, (text, emb) in enumerate(zip(texts, embeddings)):
            data.append({
                "id": f"doc_{i}",
                "vector": emb.tolist(),
                "meta": {"text": text}
            })

        try:
            self.index.upsert(data)
            print("Data inserted into Endee")
            self.data_loaded = True
        except Exception as e:
            print("Insert error:", e)

    def search(self, query, k=5):
        query_vec = get_embedding([query])[0].tolist()

        try:
            results = self.index.query(
                vector=query_vec,
                top_k=k
            )
            print("Search results:", results)

            return [r["meta"]["text"] for r in results]
        
        except Exception as e:
            print("Query error:", e)
            return []
