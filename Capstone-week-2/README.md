# Sakoonify API v0.2

Sakoonify is an AI mental health companion backend built with FastAPI.

## Features

- Health check
- Validated chat endpoint
- User session history
- Audio file upload
- MP3/WAV validation
- 10 MB upload limit
- Logging
- Error handling
- Clean project structure

## Project Structure

```text
sakoonify-api/
│
├── main.py
├── models.py
├── sessions.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── uploads/
└── history.json