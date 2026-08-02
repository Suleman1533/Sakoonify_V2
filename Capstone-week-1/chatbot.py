from session import Session


class ChatBot:
    def __init__(self):
        self.session = Session()
        self.running = True

    def start(self):
        print("=" * 50)
        print("Welcome to Sakoonify CLI")
        print("Type /help to see available commands.")
        print("=" * 50)

        while self.running:            
            message = self.get_user_input()
                        
            if not message.strip():
                continue
            
            if self.process_command(message):
                continue
            
            self.session.add_message("user", message)
            
            reply = self.generate_reply(message)
            
            self.session.add_message("assistant", reply)
            
            print(f"\nAI: {reply}\n")

    def get_user_input(self):
        return input("You: ")

    def process_command(self, message):

        if message == "/help":
            print("\nAvailable Commands")
            print("------------------")
            print("/help      Show commands")
            print("/history   Show chat history")
            print("/clear     Clear chat history")
            print("/exit      Exit chatbot\n")
            return True

        elif message == "/history":
            self.session.show_history()
            return True

        elif message == "/clear":
            self.session.clear_history()
            print("History cleared.\n")
            return True

        elif message == "/exit":
            print("Goodbye!")
            self.running = False
            return True

        return False

    def generate_reply(self, message):
        message = message.lower()

        if "happy" in message or "good" in message or "great" in message:
            return "😊 That's wonderful! I'm really glad you're feeling good."

        elif "sad" in message or "depressed" in message or "upset" in message:
            return "💙 I'm sorry you're feeling that way. I'm here to listen."

        elif "hello" in message or "hi" in message:
            return "👋 Hello! How are you today?"

        elif "thank" in message:
            return "😊 You're very welcome!"

        elif "bye" in message:
            return "Take care! Have a wonderful day."

        else:
            return f"You said: {message}"