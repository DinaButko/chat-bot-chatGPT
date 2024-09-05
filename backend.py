import openai


class ChatBot:

    def __init__(self, api_key):
        openai.api_key = api_key

    def get_response(self, user_input):
        response = openai.completions.create(  # Using the new "completions.create" method
            model="gpt-4o-mini",  # Use the correct model name
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    # Replace 'your-api-key' with your actual OpenAI API key
    chatbot = ChatBot(
        api_key="")
    response = chatbot.get_response("Write a joke about QA.")
    print(response)
