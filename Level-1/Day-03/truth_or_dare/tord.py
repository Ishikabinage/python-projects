import random

truths = [
    "What is your biggest fear?",
    "Have you ever lied to your best friends?",
    "What is your most embrassing moments",
    "who do you like the most?",
    "what is your secret talent?",
]

dares = [
    "Do 10 pushups",
    "sing a song loudly",
    "Dance for a 30 seconds",
    "Act like a monkey for 1 minute",
    "Talk in a funny voice for 2 mins",
]

print("Welcome to Truth and Dare Game!")

while True:
    choice = input("\n choose Truth or Dare( or 'q' to quit):").lower()

    if choice == "truth":
        print("\n Truth:")
        print(random.choice(truths))
    elif choice == "dare":
        print("\n Dare:")
        print(random.choice(dares))

    elif choice == "q":
        print("GoodBye!")
        break
    else:
        print("Invalid choice. Try again.")