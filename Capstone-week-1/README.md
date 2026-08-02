# 🤖 Sakoonify CLI — Week 1 Capstone

> *"From zero to a production-ready CLI chatbot in 7 days."*

---

## 📖 The Story Behind This Project

This isn't just a chatbot. It is the **physical proof** of my first week on the **AI-300 (Azure AI Engineer) 70-day challenge**.

Exactly 7 days ago, I opened a blank Python file and typed `for i in range(1, 51):`. Today, I am closing the week by writing a fully object-oriented CLI application that saves data to JSON, handles errors gracefully, and uses professional logging.

**This README is not just about the code. It is about the journey.**

---

## 🗓️ The 7-Day Learning Sprint

I didn't build this in one day. I built it layer by layer, following a strict daily discipline:

| Day | Focus Area | What I Built / Learned |
| :--- | :--- | :--- |
| **Day 1** | Python Basics | Loops, functions, `is_prime()`, and set up my Azure account. |
| **Day 2** | Data Structures | Lists, dicts, string methods, and `collections.Counter`. |
| **Day 3** | Git & Functions | `*args`, `lambda`, `sorted()`, and my first 3 Git commits. |
| **Day 4** | OOP Part 1 | `class`, `__init__`, `self`, methods, and attributes (`BankAccount`, `Student`). |
| **Day 5** | OOP Part 2 | Inheritance (`super()`), method overriding (`Vehicle` → `Car`/`Bike`). |
| **Day 6** | File I/O & Logging | `json.dump()`, `json.load()`, `try/except`, and replacing `print()` with `logging`. |
| **Day 7** | Capstone | Integrated everything into a single, clean CLI application (**this project**). |

---

## 📚 The "Flashcard" Methodology (My Secret Weapon)

To ensure I *actually* retained everything (and didn't just "copy-paste"), I used the **Anki flashcard system** every single day.

Here are the core concepts I drilled repeatedly to build muscle memory:

- **OOP Concepts:** What is `self`? What does `__init__` do? Class vs Object?
- **Git Essentials:** `add`, `commit`, `log`, and why commit messages matter.
- **File Handling:** The difference between `"r"` and `"w"` mode. Catching `FileNotFoundError`.
- **JSON:** Converting Python dicts to JSON strings and back.
- **Logging:** Why `logging.info()` is better than `print()` for production apps.

---

## 🚀 Features

- 💬 **Chat Interface:** Talk to a simple rule-based AI.
- 💾 **JSON Persistence:** Your chat history is saved automatically and reloaded when you restart the app.
- 📜 **History Command:** View your entire conversation with `/history`.
- 🗑️ **Clear Command:** Wipe the chat history with `/clear`.
- 🛑 **Exit:** Close the app cleanly with `/exit`.
- 📝 **Professional Logging:** Every action (load, save, error) is timestamped for debugging.

---

## 🏗️ Project Structure
