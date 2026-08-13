from embeddings import EmbeddingModel
from vector_store import VectorStore


embedding_model = EmbeddingModel()

vector_store = VectorStore(
    dimension=384,
)


memories = [
    "User prefers EUR/USD.",
    "User prefers risk below 1%.",
    "User likes pizza.",
]


for memory in memories:
    embedding = embedding_model.encode(memory)

    vector_store.add(
        embedding,
        memory,
    )


query = "Which currency pair does the user prefer?"

query_embedding = embedding_model.encode(query)

results = vector_store.search(
    query_embedding,
    k=2,
)

print("Relevant memories:")

for result in results:
    print("-", result)