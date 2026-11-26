
from datetime import datetime
print("================================")
print("     SMART GREETING BOT")
print("================================")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hour = datetime.now().hour
if hour < 12:
    greeting = "Good Morning❤️"
elif hour < 17:
    greeting = "Good Afternoon🧡"
else:
    greeting = "Good Evening💛"
print(f"\n{greeting }, {name}!")
mood = input("How are you feeling today? ").lower()
if mood == "happy":
    print(f"That's wonderful, {name}! Keep smiling!😊")
elif mood == "sad":
    print("Don't worry! Every day brings a new hope.")
elif mood == "tired":
    print("Take some rest. You deserve a break!")
elif mood == "excited":
    print("Amazing! Keep your energy high!")
else:
    print("Thank you for sharing your feelings!")
if age < 18:
    print("Keep learning and exploring!")
elif age <= 25:
    print("Enjoy your learning journey and build your future!")
else:
    print("Keep growing and achieving your goals!")

print("\nHave a wonderful day!")
print("================================")
