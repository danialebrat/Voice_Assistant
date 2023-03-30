import random

# Define possible user inputs and corresponding chatbot responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing great, thanks for asking!", "I'm fine, how are you?", "I'm doing well!"],
    "what's your name": ["My name is Chatbot!", "I'm Chatbot, nice to meet you!"],
    "goodbye": ["Goodbye!", "See you later!", "Bye!"]
}

# Define a function to handle user input and generate chatbot response
def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "I'm sorry, I don't understand."

# Use a while loop to keep the chatbot running until the user types "goodbye"
print("Hello, I'm Chatbot! How can I help you?")
while True:
    user_input = input()
    if user_input == "goodbye":
        print(chatbot_response(user_input))
        break
    else:
        print(chatbot_response(user_input))
