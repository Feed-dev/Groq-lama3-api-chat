import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

client = Groq(
    api_key=os.getenv('GROQ_API_KEY'),
)

topic = ""

while topic != "stop":
    topic = input("\nEnter the topic you want to research: ")
    if topic == "stop":
        break
    else:
        stream = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "you are a research assistant."
                },
                {
                    "role": "user",
                    "content": f"{topic}",
                }
            ],
            model="llama3-70b-8192",
            max_tokens=1024,
            temperature=0.5,
            top_p=1,
            stop=None,
            stream=True,
        )

        for chunk in stream:
            print(chunk.choices[0].delta.content, end="")
