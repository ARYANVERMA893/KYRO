from memory.manager import MemoryManager
from ollama import OllamaClient


memory_manager = MemoryManager()
ollama = OllamaClient()


memory_manager.save_memory(
    "User prefers EUR/USD."
)

memory_manager.save_memory(
    "User prefers risk below 1%."
)


question = "What currency pair do I prefer?"


relevant_memories = (
    memory_manager.retrieve_relevant_memories(
        question,
        k=2,
    )
)


memory_context = "\n".join(
    f"- {memory}"
    for memory in relevant_memories
)


messages = [
    {
        "role": "system",
        "content": (
            "You are KYRO, a local AI assistant. "
            "Use the provided memories when they are "
            "relevant to the user's question."
        ),
    },
    {
        "role": "user",
        "content": (
            f"Relevant memories:\n"
            f"{memory_context}\n\n"
            f"Question: {question}"
        ),
    },
]


answer = ollama.chat(messages)

print("KYRO:", answer)