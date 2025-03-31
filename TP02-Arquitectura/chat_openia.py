from openai import OpenAI

client = OpenAI()

context = ""

def chat_with_gpt(user_query):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": user_query}
            ],
            temperature=1,
            max_tokens=16384,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"
        exit()

def main():
    try:
        user_query = input("You: ")
        if user_query.strip():
            print(f"You: {user_query}")
            response = chat_with_gpt(user_query)
            print(f"ChatGPT: {response}")
        else:
            print("ChatGPT: Bye!")
            exit()
    except Exception as e:
        print(f"Error: {e}")
        exit()

if __name__ == "__main__":
    main()
