# RULE-BASED AI CHATBOT
# DecodeLabs Internship Project 1

responses = {
    "hello": "Hello! Welcome!",
    "hi": "Hi! How can I help you?",
    "how are you": "I am doing great!",
    "what is your name": "I am your AI Chatbot.",
    "help": "Sure! Tell me what you need.",
    "good morning": "Good morning! Have a nice day!",
    "thank you": "You are welcome!",
    "bye": "Goodbye! Have a nice day!"
}

print("================================")
print("       AI CHATBOT")
print("================================")
print("Type 'exit' to stop chatting.")

while True:

    user_input = input("You: ").lower().strip()

    if user_input == "exit":
        print("Bot: Thank you for chatting!")
        break

    elif user_input in responses:
        print("Bot:", responses.get(user_input))

    else:
        print("Bot: Sorry, I don't understand that.")