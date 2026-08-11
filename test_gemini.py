from config import client

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Hello! Introduce yourself in one sentence."
)

print(response.text)