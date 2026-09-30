import httpx

response = httpx.get("https://api.github.com/users/octocat", timeout=10.0)
response.raise_for_status()

data = response.json()
print(response.status_code, data["name"])