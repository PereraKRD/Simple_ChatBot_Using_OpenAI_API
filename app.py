from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

client = OpenAI()

print("=============== Welcome To SoftG Bot PlatForm ================")

while True : 
    question = input("User : ")
    if question != "Bye":
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            max_tokens=50,
            n=1,
            temperature=0.3,
            messages=[
                {"role" : "user", "content" : question}
            ]
        )

        for choice in response.choices:
            print(f"SoftG Bot : {choice.message.content}")

    else:
        print("SoftG Bot : Bye...")
        break