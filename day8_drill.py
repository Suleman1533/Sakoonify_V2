import requests

url = "https://api.github.com/repos/Suleman1533/Sakoonify_V2/contents/"
response = requests.get(url)

print(response.status_code)
print(response.json()) 

print("=" * 50)

class User:
    def __init__(self, user_name):
        self.user_name = user_name


# Session inherits from User
class Session(User):
    def __init__(self, user_name):
        super().__init__(user_name)
        self.history = []

    def add_message(self, message):
        self.history.append(message)


# Dictionary storing Session objects
sessions = {}

sessions["101"] = Session("Suleman")
sessions["102"] = Session("Ahmad")

# Safe lookup
session = sessions.get("101")

if session:
    session.add_message("Hello!")
    print(session.user_name)
    print(session.history)
else:
    print("Session not found.")