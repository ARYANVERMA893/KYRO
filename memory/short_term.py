class ShortTermMemory:
    def __init__(self) -> None:
        self.messages: list[dict[str, str]] = []

    def add_user_message(self, message: str) -> None:
        self.messages.append(
            {
                "role": "user",
                "content": message,
            }
        )

    def add_assistant_message(self, message: str) -> None:
        self.messages.append(
            {
                "role": "assistant",
                "content": message,
            }
        )

    def get_messages(self) -> list[dict[str, str]]:
        return self.messages

    def clear(self) -> None:
        self.messages.clear()