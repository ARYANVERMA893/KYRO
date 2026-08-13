from manager import MemoryManager

memory_manager = MemoryManager()


memory_manager.save_memory(
    "User prefers EUR/USD."
)

memory_manager.save_memory(
    "User prefers risk below 1%."
)

memory_manager.save_memory(
    "User likes pizza."
)


query = "Which currency pair does the user prefer?"

results = memory_manager.retrieve_relevant_memories(
    query,
    k=2,
)


print("Relevant memories:")

for memory in results:
    print("-", memory)