import random

print("🤖 Chatbot: Hello! Type 'exit' to end the chat.\n")

responses =[
    "That's interesting!",
    "Tell me more.",
    "I see!",
    "Hmm... okay.",
    "Can you explain that?",
    "Wow, really?",
    "That sounds fun!",
    "I'm not sure, but keep going!"
]

while True:
    user_input = input("You:").lower()

    if user_input =="exit":
        print("🤖 chatBot : Goodbye!")
        break

    elif user_input == "exit":
        print("🤖 ChatBot: Hello there! 😊")

    elif "how are you" in user_input:
        print("🤖 ChatBot: I'm just code, but I'm doing great!")

    elif "your name" in user_input:
        print("🤖 ChatBot: I'm your Python ChatBot 🤖")

    else:
        print("🤖 ChatBot:", random.choice(responses)) 