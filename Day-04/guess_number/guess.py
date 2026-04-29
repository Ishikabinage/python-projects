import random

print("Welcome to Guess My Number")

print("\n choose difficulty:")
print("1. Easy(1-50, 10 attempts)")
print("2. Medium(1-100, 7 attempts)")
print("1. Hard(1-200, 5 attempts)")

choice = input("Enter choice(1/2/3):")

if choice == "1":
    number = random.randint(1,50)
    attempts = 10
elif choice ==  "2":
    number = random.randint(1,100)
    attempts = 7
elif choice == "3":
    number = random.randint(1,200)
    attempts = 5
else:
    print("Invalid choice")
    exit()

print("\n I have selected a number : start guessing!")

while attempts > 0:
    try:
        guess = int(input(f"Enter your guess({attempts} attempts left):"))
    except ValueError:
        print("❌ Please Enter a valid number!")
        continue

    if guess < number:
        print("too low!")
    elif guess< number:
        print("Too high")
    else:
        print("🎉 correct! You guessed it!")
        break

    attempts -=1

if attempts == 0 and guess != number:
    print(f"You lost! The number was {number}")