with open("Saifullah.txt" ,"w") as file :
    file.write("Great Saif")
    
with open("Saifullah.txt" ,"r") as file :
    print(file.read())
print("=========================================================================")

import json

history = [{"role" : "user" , "text" : "happy"}]

with open("history.json" , "w") as f:
    json.dump(history,f)
    
# Load
with open("history.json", "r") as f:
    loaded_history = json.load(f)
    print(loaded_history)  # Output: [{'role': 'user', 'text': 'happy'}]
    
print("=========================================================================")
import json

# 1. Create a Python object
my_data = {
    "user": "Suleman",
    "scores": [95, 87, 92],
    "is_active": True
}

# 2. SAVE: Python → JSON → File
with open("test.json", "w") as f:
    json.dump(my_data, f, indent=5)
print("✅ Saved to test.json")

# 3. LOAD: File → JSON → Python
with open("test.json", "r") as f:
    loaded_data = json.load(f)
print("✅ Loaded from test.json")
print(loaded_data)

# 4. Verify it's the same
print(my_data == loaded_data)  # Should print True
import json
import logging

# Configure logging (adds timestamps to all messages)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Session:
    def __init__(self, user_name):
        self.user_name = user_name
        self.history = []
        self.filename = "history.json"  # File to store chat history
        
        # TRY to load existing history. If file doesn't exist, start fresh.
        try:
            with open(self.filename, "r") as f:
                self.history = json.load(f)
            logging.info(f"Loaded {len(self.history)} messages from {self.filename}")
        except FileNotFoundError:
            logging.warning(f"No history file found. Starting fresh for {user_name}.")
            self.history = []
        except json.JSONDecodeError:
            logging.error("History file is corrupted. Starting fresh.")
            self.history = []

    def add_message(self, role, text):
        self.history.append({"role": role, "text": text})
        self._save_history()  # Auto-save after every message

    def get_reply(self, mood):
        if mood.lower() == "happy":
            return f"Alhamdulillah, {self.user_name}! Keep smiling!"
        elif mood.lower() == "sad":
            return f"Hey {self.user_name}, it's okay to feel sad. You are not alone."
        else:
            return f"Thank you for sharing, {self.user_name}. I'm here to listen."

    def show_history(self):
        if not self.history:
            logging.info("No messages in history.")
            return
        for entry in self.history:
            print(f"{entry['role']}: {entry['text']}")

    def _save_history(self):
        #self.history.append({"role": role, "text": text})
        """Internal method: saves current history to JSON file."""
        try:
            with open(self.filename, "w") as f:
                json.dump(self.history, f, indent=4)
            logging.info(f"Saved {len(self.history)} messages to {self.filename}")
        except Exception as e:
            logging.error(f"Failed to save history: {e}")

if __name__ == "__main__":
    # Test the upgraded Session
    session = Session("Suleman")
    session.add_message("user", "happy")
    reply = session.get_reply("happy")
    session.add_message("bot", reply)
    session.show_history()