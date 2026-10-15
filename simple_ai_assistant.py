
from pyexpat.errors import messages

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY"),
)

message = []
message.append(
    {
        "role": "system",
        "content": "Act like a very humble agent and respond always under 20 words."
    }
)


while True:

    user_input = input("\nshuba:")

    if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
        break

    message.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=message
    )

    message.append({
        "role": "assistant",
        "content": response.choices[0].message.content
    })

    print("Assistant: " + response.choices[0].message.content)