import random


questions = [
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "Who is known as the father of computers?",
        "options": ["A. Charles Babbage", "B. Alan Turing", "C. Elon Musk", "D. Bill Gates"],
        "answer": "A"
    },
    {
        "question": "Which data structure uses FIFO?",
        "options": ["A. Stack", "B. Queue", "C. Tree", "D. Graph"],
        "answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Control Processing Unit"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. def", "C. fun", "D. define"],
        "answer": "B"
    },
]

random.shuffle(questions)
score = 0

print("❓ Welcome to the Quiz Game!\n")

for q in questions:
    print(q["question"])
    
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer is {q['answer']}\n")

print("🎯 Quiz Completed!")
print(f"Your final score: {score}/{len(questions)}")