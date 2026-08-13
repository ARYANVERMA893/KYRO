from sentence_transformers import SentenceTransformer


class EmbeddingModel:
    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2",
    ) -> None:
        self.model = SentenceTransformer(model_name)

    def encode(self, text: str) -> list[float]:
        embedding = self.model.encode(text)

        return embedding.tolist()