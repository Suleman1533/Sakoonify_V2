import json,logging

class Session:
    def __init__(self):
        self.history = []
        self.file = "Sakoonify.json"

        self.load_history()

    def load_history(self):
        try:
            with open(self.file, "r") as f:
                self.history = json.load(f)
            logging.info("History loaded successfully.")

        except FileNotFoundError:
            self.history = []
            logging.info("History file not found.")

        except json.JSONDecodeError:
            self.history = []
            logging.warning("History file is corrupted.")
            
    def save_history(self):
        try:
            with open(self.file, "w") as f:
                json.dump(self.history , f, indent=4)
            logging.info("History Saved Successfully.")

        except Exception as e:
            logging.error(f"Error saving history : {e}")
    
    def add_message(self, role, message):
        self.history.append({
            "role": role,
            "message": message
        })
        self.save_history()
        
    def show_history(self):
        for chat in self.history:
            print(f"{chat['role']} : {chat ['history']}")
            
    def clear_history(self):
        self.history.clear()
        self.save_history()
        logging.info("History cleared successfully.")