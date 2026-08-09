import requests

response = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "qwen3:8b",
        "messages": [
            {
                "role": "user",
                "content": "Explain what RSI means."
            }
        ],
        "stream": False,
    },
)

data = response.json()

print(data["message"]["content"])