
import os
from dotenv import load_dotenv
from chatbot2 import ChatBot
load_dotenv()
bot_name = os.getenv("BOT_NAME", "ChatMate")
bot = ChatBot(bot_name)
print(bot)
bot.load_history()
print("\nWelcome to ChatMate!")
print("Type 'bye' to exit.\n")
while True:
    user_message = input("You: ")
    if not user_message.strip():
        print("Please enter a message.")
        continue
    bot.add_message("user", user_message)
    reply = bot.get_reply(user_message)
    print(bot.bot_name + ":", reply)
    bot.add_message("bot", reply)
    if user_message.lower().strip() == "bye":
        break
bot.save_history()
print("\nChat history saved successfully!")
