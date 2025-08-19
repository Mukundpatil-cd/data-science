quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Paris", "C. Madrid", "D. Rome"],
        "answer": "B"
    },
    {
        "question": "Which language is used for Data Science?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. Java"],
        "answer": "A"
    },
    {
        "question": "What is 7 * 8?",
        "options": ["A. 54", "B. 56", "C. 64", "D. 58"],
        "answer": "B"
    },
    {
        "question": "Who is the CEO of Tesla?",
        "options": ["A. Jeff Bezos", "B. Elon Musk", "C. Bill Gates", "D. Sundar Pichai"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. def", "B. function", "C. lambda", "D. define"],
        "answer": "A"
    }
]
score = 0

print("🧠 Welcome to the Quiz App!\n")

for idx, q in enumerate(quiz):
    print(f"Q{idx+1}: {q['question']}")
    for option in q['options']:
        print(option)
    answer = input("Your answer (A/B/C/D): ").strip().upper()

    if answer == q['answer']:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer is: {q['answer']}\n")

print(f"🎉 Quiz Completed! You scored {score} out of {len(quiz)}.")