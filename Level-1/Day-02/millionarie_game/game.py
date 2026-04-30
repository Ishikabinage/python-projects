questions =[
["What is the capital of India?", "A.Mumabi","B. Delhi","C. Chennai", "D.kolkata","B"],
 ["Which language is used for web apps?", "A. Python", "B. Java", "C. JavaScript", "D. All", "D"],
    ["2 + 2 = ?", "A. 3", "B. 4", "C. 5", "D. 6", "B"]
]

money = 0

print("Welcome to who wants to be a Millionarie!\n")

for q in questions:
    print(q[0])
    print(q[1])
    print(q[2])
    print(q[3])
    print(q[4])

    answer = input("Enter your answer(A/B/C/D):").upper()

    if answer == q[5]:
        money += 1000
        print(f"✅ correct! You win ₹{money}\n")
    else:
        print("❌ Wrong answer!")
        print(f"You take home ₹{money}")
        break

print("Game Over")