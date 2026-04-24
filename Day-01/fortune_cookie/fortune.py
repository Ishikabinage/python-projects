import random

fortunes = [
    "you will have a great day!",
    "Success is coming your way.",
    "you will learn something new today.",
    "A pleasant suprise is waiting for you.",
    "Hard work pays off soon.",
    "Happiness begins with you.",
    "Good new is on the way!",
    "Believe in yourself and achieve greatness."
]

print("Welcome to Fortune Cookie!")

input("Press Enter to get your fortune..")

fortune= random.choice(fortunes)

print("\n 🌟 Your Fortune:")
print(fortune)