from short_term import ShortTermMemory
from long_term import LongTermMemory
from embeddings import EmbeddingModel
from vector_store import VectorStore

class MemoryManager:
    def __init__(self) -> None:
        self.short_term = ShortTermMemory()
        self.long_term = LongTermMemory()
        self.embedding_model = EmbeddingModel()

        self.vector_store = VectorStore(
            dimension=384,
        )
    def add_user_message(self, message: str) -> None:
        self.short_term.add_user_message(message)

    def add_assistant_message(self, message: str) -> None:
        self.short_term.add_assistant_message(message)

    def save_memory(self, memory: str) -> None:
        self.long_term.save(memory)

        embedding = self.embedding_model.encode(memory)

        self.vector_store.add(
            embedding,
            memory,
        )

    def get_conversation(self) -> list[dict[str, str]]:
        return self.short_term.get_messages()

    def get_memories(self) -> list[dict[str, str]]:
        return self.long_term.get_all()
    def retrieve_relevant_memories(
        self,
        query: str,
        k: int = 3,
    ) -> list[str]:

        query_embedding = self.embedding_model.encode(
            query
        )

        return self.vector_store.search(
            query_embedding,
            k=k,
        )