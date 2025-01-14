import openai
def chatbot():
    openai.api_key = "API_KEY"

    print("Welcome to the OpenAI Chatbot!")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=100
            )

            assistant_reply = response.choices[0].message.content
            print(f"Chatbot: {assistant_reply}")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    chatbot()
