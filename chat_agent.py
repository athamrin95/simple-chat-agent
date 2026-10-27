import os
import sys
from openai import OpenAI
from dotenv import load_dotenv


def call_ai(client:OpenAI, messages:str, openrouter_model:str) -> str:
    reply:str
    try:
        response = client.chat.completions.create(
            model=openrouter_model,
            messages=messages,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main() -> None:
    load_dotenv()
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
    openrouter_base_url = os.getenv("OPENROUTER_BASE_URL")
    openrouter_model = os.getenv("OPENROUTER_MODEL")
    if any(value is None or value == "" for value in(openrouter_api_key, openrouter_base_url, openrouter_model)):
        print(f"OPENROUTER_API_KEY, OPENROUTER_BASE_URL, and/or OPENROUTER_MODEL is missing or cannot be read from your .env file. Exiting...")
        sys.exit(1)

    client = OpenAI(api_key=openrouter_api_key, base_url=openrouter_base_url)
    print(f"This is a chat terminal for communicating with A.I. model '{openrouter_model}'")
    messages = []
    while True:
        user_input = input("Your input (Type 'keluar' to exit): ")
        if user_input.strip().lower() == 'keluar':
            break
        if user_input.strip() == '':
            print(f"You've entered an empty command, please try again.")
            continue
        
        messages.append({"role": "user", "content": user_input})
        reply = call_ai(client, messages, openrouter_model)
        if reply:
            print(reply)
            messages.append({"role": "assistant", "content": reply})
            

if __name__ == "__main__":
    main()

