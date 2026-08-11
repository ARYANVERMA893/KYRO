from memory.short_term import ShortTermMemory
from memory.long_term import LongTermMemory


class MemoryManager:
    def __init__(self) -> None:
        self.short_term = ShortTermMemory()
        self.long_term = LongTermMemory()

    def add_user_message(self, message: str) -> None:
        self.short_term.add_user_message(message)

    def add_assistant_message(self, message: str) -> None:
        self.short_term.add_assistant_message(message)

    def save_memory(self, memory: str) -> None:
        self.long_term.save(memory)

    def get_conversation(self) -> list[dict[str, str]]:
        return self.short_term.get_messages()

    def get_memories(self) -> list[dict[str, str]]:
        return self.long_term.get_all()