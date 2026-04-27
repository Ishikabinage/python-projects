print("You are standing in front of a dark forest.")

choice1 = input("Do you want to go LEFT or RIGHT?").lower()

if choice1 == "left":
    print("\n You walk into the forest and see a river.")

    choice2 = input("Do you Swim or wait?").lower()

    if choice2 == "wait":
        print("\n A boat arrives and takes you safely across. YOU WIN!")
    elif choice2 == "swim" :
        print("\n you were attacked by a crocodile. GAME OVER")
    else:
        print("\n Invalid choice. GAME OVER")

elif choice1 == "right":
    print("\n You fall into pit . Game over")
else:
    print("\n Invalid choice.Game Over.")