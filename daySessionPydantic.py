import json
import logging

logging.basicConfig(level=logging.INFO)


class Session:

    def __init__(self):

        self.filename = "history.json"
        self.history = []

        try:
            with open(self.filename, "r") as file:
                self.history = json.load(file)

            logging.info("History loaded successfully.")

        except FileNotFoundError:

            logging.warning("History file not found. Creating a new one...")

            self.history = []

            self.save_history()

        except json.JSONDecodeError:

            logging.error("History file is corrupted.")

            self.history = []

            self.save_history()

        except Exception as e:

            logging.error(f"Unexpected Error: {e}")

            self.history = []

    def add_message(self, user_id, message):

        chat = {
            "user_id": user_id,
            "message": message
        }

        self.history.append(chat)

        self.save_history()

        logging.info("Message added successfully.")

    def save_history(self):

        try:

            with open(self.filename, "w") as file:

                json.dump(self.history, file, indent=4)

            logging.info("History saved successfully.")

        except Exception as e:

            logging.error(f"Unable to save history: {e}")

    def get_history(self):

        return self.history