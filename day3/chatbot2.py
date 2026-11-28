
import json
from typing import List, Dict
class ChatBot:
    def __init__(self, bot_name: str):
        self.bot_name = bot_name
        self.history: List[Dict[str, str]] = []
    def __str__(self) -> str:
        return f"ChatBot Name: {self.bot_name}"
    def add_message(self, role: str, content: str) -> None:
        message = {"role": role, "content": content}
        self.history.append(message)
    def get_reply(self, message: str) -> str:
        message = message.lower().strip()
        if "hello" in message or "hi" in message:
            return f"Hello! I am {self.bot_name}. How can I help you?"

        elif "python" in message:
            return "Python is a popular programming language."

        elif "study" in message:
            return "Make a timetable and practise every day!"

        elif "bye" in message:
            return "Goodbye! Have a nice day!"

        else:
            return "Sorry, I don't understand. Ask me something else."
    def save_history(self, filename: str = "chat_history.json") -> None:
        with open(filename, "w") as file:
            json.dump(self.history, file, indent=4)
    def load_history(self, filename: str = "chat_history.json") -> None:
        try:
            with open(filename, "r") as file:
                self.history = json.load(file)
        except FileNotFoundError:
            print("Chat history file not found. Starting a new conversation.")
        except json.JSONDecodeError:
            print("Invalid JSON file. Starting a new conversation.")
# Inheritance example
class FriendlyChatBot(ChatBot):
    def get_reply(self, message: str) -> str:
        reply = super().get_reply(message)
        return reply + " 😊"
