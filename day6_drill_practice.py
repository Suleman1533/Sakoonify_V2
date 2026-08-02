import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TextFileHandler:

    def __init__(self, filename):
        self.filename = filename

        try:
            with open(self.filename, "r") as file:
                self.content = file.readlines()

            logging.info("Text file loaded successfully.")

        except FileNotFoundError:
            logging.warning("Text file not found. Creating a new one...")

            self.content = [
                "Hello Suleman\n",
                "Welcome to Python\n",
                "This is your first text file.\n"
            ]

            with open(self.filename, "w") as file:
                file.writelines(self.content)

            logging.info("New text file created.")

    def show(self):
        print("----- File Content -----")

        for line in self.content:
            print(line, end="")

    def count_lines(self):
        print(f"\nTotal Lines: {len(self.content)}")


obj = TextFileHandler("history.txt")

obj.show()

obj.count_lines()

a ="""import json
import logging

logging.basicConfig(level=logging.INFO)


class JSONFileHandler:

    def __init__(self, filename):
        self.filename = filename

        try:
            with open(self.filename, "r") as file:
                self.data = json.load(file)

            logging.info("JSON file loaded successfully.")

        except FileNotFoundError:
            logging.warning("JSON file not found. Creating a new one...")

            self.data = {
                "name": "Suleman",
                "course": "Python",
                "age": 22
            }

            with open(self.filename, "w") as file:
                json.dump(self.data, file, indent=4)

            logging.info("New JSON file created.")

        except json.JSONDecodeError:
            logging.error("JSON file is corrupted.")

            self.data = {}

    def show(self):
        print("\nJSON Data")

        for key, value in self.data.items():
            print(f"{key} : {value}")


obj = JSONFileHandler("history.json")

obj.show()"""