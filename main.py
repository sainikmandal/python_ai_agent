import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv


def main():
    load_dotenv()

    args = sys.argv[1:]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "Hey! write your prompt here"')
        print('Example: python main.py "How do I forget the trauma of React?"')
        sys.exit(1)
    user_prompt = " ".join(args)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    if "--verbose" in args:
        generate_verbose_content(client, messages)
    generate_content(client, messages)


def generate_content(client, messages):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    print("Response:")
    print(response.text)

def generate_verbose_content(client, messages):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
     
    for message in messages:
        if message.role == 'user':
            for part in message.parts:
                if part.text:
                    print(f"User prompt: {part.text}")
    print("Response:")
    print(response.text)
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)






if __name__ == "__main__":
    main()

