import random

cards=[2,3,4,5,6,7,8,9,10,11]

player_cards =[random.choice(cards), random.choice(cards)]
computer_cards=[random.choice(cards), random.choice(cards)]

player_score = sum(player_cards)
computer_score = sum(computer_cards)

print("Baby Blackjack\n")

print(f"Your cards: {player_cards} -> total:{player_score}")
print(f"Your cards: {computer_cards} -> total:{computer_score}")

if player_score > 21:
    print("❌ You busted! you lose.")
elif computer_score > 21:
    print("🎉 computer busted! you win")
elif player_score > computer_score:
    print("🎉 you win!")
elif player_score < computer_score:
    print("😔 You Lose!")
else:
    print("🤝 its a tie!")


