import os
import httpx

API_KEY = os.environ["GEMINI_API_KEY"]

response = httpx.post(
    "https://generativelanguage.googleapis.com/v1beta/interactions",
    headers={"x-goog-api-key": API_KEY},
    json={"model": "gemini-3.1-flash-lite", "input": "Expalin HTTP in one sentence. "},
    timeout=60.0
)

response.raise_for_status()


data = response.json()
for step in data["steps"]:
    if step["type"] == "model_output":
        print(step["content"][0]["text"])