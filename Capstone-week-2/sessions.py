import json
import logging

from config import HISTORY_FILE


class Session:
    def __init__(self):
        self.history = {}

        try:
            if HISTORY_FILE.exists():
                with open(HISTORY_FILE, "r", encoding="utf-8") as file:
                    self.history = json.load(file)

                logging.info("History loaded successfully.")

            else:
                logging.info("No history file found. Starting fresh.")
                self._save_history()

        except json.JSONDecodeError:
            logging.error("History file is corrupted. Starting fresh.")
            self.history = {}
            self._save_history()

        except Exception as e:
            logging.error(f"Failed to load history: {e}")
            self.history = {}

    def add_message(self, user_id, role, message):
        if user_id not in self.history:
            self.history[user_id] = []

        self.history[user_id].append({
            "role": role,
            "message": message
        })

        self._save_history()

        logging.info(f"Message saved for user {user_id}")

    def get_history(self, user_id):
        return self.history.get(user_id, [])

    def clear_history(self, user_id):
        self.history[user_id] = []
        self._save_history()

    def _save_history(self):
        try:
            with open(HISTORY_FILE, "w", encoding="utf-8") as file:
                json.dump(self.history, file, indent=4)

            logging.info("History saved successfully.")

        except Exception as e:
            logging.error(f"Failed to save history: {e}")
            raise