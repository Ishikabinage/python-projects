import random

while True:
    choice = input("Roll dice ? (y/n):").lower()

    if choice == 'y':
        print("you rolled:", random.randint(1,6))
    else:
        print("Game ended")
        break