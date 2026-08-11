import json
from pathlib import Path


class LongTermMemory:
    def __init__(self, file_path: str = "memory/memories.json") -> None:
        self.file_path = Path(file_path)
        self.memories: list[dict[str, str]] = []

        self._load()

    def _load(self) -> None:
        if not self.file_path.exists():
            return

        with self.file_path.open("r", encoding="utf-8") as file:
            self.memories = json.load(file)

    def save(self, memory: str) -> None:
        self.memories.append(
            {
                "memory": memory,
            }
        )

        self._write()

    def get_all(self) -> list[dict[str, str]]:
        return self.memories

    def _write(self) -> None:
        self.file_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(
                self.memories,
                file,
                indent=4,
            )