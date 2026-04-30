import random

options = ["rock","paper","scissors","lizard","spock"]

print("Rock Paper Scissors Lizard Spock Game")

user = input("Enter rock, paper, scissors,lizard or spock:").lower()

if user not in options:
    print("Invalid choice!")
else:
    computer = random.choice(options)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif(
        (user== "scissors" and computer=="paper") or
        (user== "paper" and computer=="rock") or
        (user== "rock" and computer=="lizard") or
        (user== "lizard" and computer=="spock") or
        (user== "spock" and computer=="scissors") or
        (user== "scissors" and computer=="lizard") or
        (user== "lizard" and computer=="paper") or
        (user== "paper" and computer=="spock") or
        (user== "spock" and computer=="rock") or
        (user== "rock" and computer=="scissors") 
    ):
        print("you win!🎉")