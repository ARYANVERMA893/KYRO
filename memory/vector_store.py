import faiss
import numpy as np


class VectorStore:
    def __init__(self, dimension: int) -> None:
        self.dimension = dimension

        self.index = faiss.IndexFlatL2(dimension)

        self.memories: list[str] = []

    def add(
        self,
        embedding: list[float],
        memory: str,
    ) -> None:
        vector = np.array(
            [embedding],
            dtype=np.float32,
        )

        self.index.add(vector)

        self.memories.append(memory)

    def search(
        self,
        embedding: list[float],
        k: int = 3,
    ) -> list[str]:

        if self.index.ntotal == 0:
            return []

        vector = np.array(
            [embedding],
            dtype=np.float32,
        )

        k = min(k, self.index.ntotal)

        distances, indices = self.index.search(
            vector,
            k,
        )

        return [
            self.memories[index]
            for index in indices[0]
            if index != -1
        ]