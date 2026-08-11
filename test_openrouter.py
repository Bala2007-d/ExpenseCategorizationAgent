from config import client

response = client.chat.completions.create(
    model="nvidia/nemotron-3-ultra-550b-a55b:free",
    messages=[
        {
            "role": "user",
            "content": "Hello! Introduce yourself in one sentence."
        }
    ]
)

print(response.choices[0].message.content)