import requests


class OllamaClient:
    def __init__(
        self,
        model: str = "qwen3:8b",
    ) -> None:
        self.url = "http://localhost:11434/api/chat"
        self.model = model

    def chat(
        self,
        messages: list[dict[str, str]],
    ) -> str:

        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "messages": messages,
                "stream": False,
            },
        )

        response.raise_for_status()

        data = response.json()

        return data["message"]["content"]