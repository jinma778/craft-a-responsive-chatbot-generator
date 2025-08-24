Python
import tkinter as tk
from tkinter import messagebox
import random

class ChatbotGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Responsive Chatbot Generator")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.intents = []
        self.responses = []

        self.intent_label = tk.Label(self.root, text="Intents:")
        self.intent_label.pack(pady=10)

        self.intent_entry = tk.Text(self.root, height=10, width=40)
        self.intent_entry.pack(pady=10)

        self.response_label = tk.Label(self.root, text="Responses:")
        self.response_label.pack(pady=10)

        self.response_entry = tk.Text(self.root, height=10, width=40)
        self.response_entry.pack(pady=10)

        self.generate_button = tk.Button(self.root, text="Generate Chatbot", command=self.generate_chatbot)
        self.generate_button.pack(pady=10)

    def generate_chatbot(self):
        self.intents = [line.strip() for line in self.intent_entry.get("1.0", "end-1c").split("\n")]
        self.responses = [line.strip() for line in self.response_entry.get("1.0", "end-1c").split("\n")]

        if len(self.intents) != len(self.responses):
            messagebox.showerror("Error", "Intents and responses must have the same number of lines.")
            return

        chatbot_code = ""
        chatbot_code += "class Chatbot:\n"
        chatbot_code += "    def __init__(self):\n"
        chatbot_code += "        self.intents = {}\n"
        chatbot_code += "        self.responses = {}\n\n"

        for intent, response in zip(self.intents, self.responses):
            chatbot_code += f"        self.intents['{intent}'] = '{response}'\n"

        chatbot_code += "\n    def respond(self, intent):\n"
        chatbot_code += "        return self.intents.get(intent, 'I didn\'t understand that.')\n\n"

        chatbot_code += "chatbot = Chatbot()\n\n"
        chatbot_code += "def run_chatbot():\n"
        chatbot_code += "    while True:\n"
        chatbot_code += "        user_input = input('> ')\n"
        chatbot_code += "        response = chatbot.respond(user_input)\n"
        chatbot_code += "        print(response)\n\n"

        chatbot_code += "run_chatbot()"

        with open("chatbot.py", "w") as f:
            f.write(chatbot_code)

        messagebox.showinfo("Success", "Chatbot generated successfully!")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    generator = ChatbotGenerator()
    generator.run()