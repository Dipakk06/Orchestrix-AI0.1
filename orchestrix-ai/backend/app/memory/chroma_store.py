from chromadb import HttpClient

from app.core.config import get_settings


class MemoryStore:
    def __init__(self) -> None:
        settings = get_settings()
        self.client = HttpClient(host=settings.chroma_host, port=settings.chroma_port)
        self.collection = self.client.get_or_create_collection(name="orchestrix_memory")

    def save(self, user_id: str, text: str, metadata: dict | None = None) -> str:
        memory_id = f"{user_id}-{abs(hash(text))}"
        self.collection.upsert(ids=[memory_id], documents=[text], metadatas=[metadata or {}])
        return memory_id

    def search(self, query: str, limit: int = 5) -> list[dict]:
        result = self.collection.query(query_texts=[query], n_results=limit)
        docs = result.get("documents", [[]])[0]
        metadatas = result.get("metadatas", [[]])[0]
        return [
            {"text": doc, "metadata": meta}
            for doc, meta in zip(docs, metadatas)
        ]
