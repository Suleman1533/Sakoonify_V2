from pathlib import Path

# Base project folder
BASE_DIR = Path(__file__).resolve().parent

# Data files/folders
HISTORY_FILE = BASE_DIR / "history.json"
UPLOAD_FOLDER = BASE_DIR / "uploads"

# Audio upload limit
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

# Allowed audio extensions
ALLOWED_AUDIO_EXTENSIONS = {".mp3", ".wav"}