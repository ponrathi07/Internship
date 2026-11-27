
print("=" * 40)
print("       STUDYBUDDY CHATBOT")
print("=" * 40)
name = input("Enter your name: ").strip()
print(f"\nHello {name}! Welcome to StudyBuddy.")
print("I am your personal study assistant.")
print("Ask me about Python, studies, exams and more.")
print("Type 'bye' to exit.")
responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi! Nice to meet you!",
    "python": "Python is a popular, easy-to-learn programming language.",
    "study": "Make a timetable and study one topic at a time.",
    "exam": "Revise important questions and practise daily.",
    "internship": "Learn new skills and complete practical projects.",
    "project": "Start with a simple idea and improve it step by step.",
    "motivation": "Believe in yourself! Small steps create big success.",
    "tired": "Take a short break and refresh your mind.",
    "thanks": "You are welcome! Happy learning!"
}
conversation = []
while True:
    message = input(f"\n{name}: ").strip().lower()
    message = message.replace("?", "").replace("!", "").replace(".", "").replace(",", "")
    if message == "":
        print("StudyBuddy: Please enter something!")
        continue
    conversation.append({
        "role": "user",
        "content": message
    })
    if message == "bye":
        reply = f"Goodbye {name}! Keep learning and achieve your dreams!"
        print(f"StudyBuddy: {reply}")
        conversation.append({
            "role": "assistant",
            "content": reply
            })
        break
    reply = "Sorry, I don't know that yet. Ask me about studies, exams or Python!"
    for keyword, answer in responses.items():
        if keyword in message.split():
            reply = answer
            break
    print(f"StudyBuddy: {reply}")
    conversation.append({
        "role": "assistant",
        "content": reply
    })
print("\n" + "=" * 40)
print("          CHAT HISTORY")
print("=" * 40)
for chat in conversation:
    print(f"{chat['role'].title()}: {chat['content']}")
print(f"\nTotal messages: {len(conversation)}")
print("Thank you for using StudyBuddy!")
