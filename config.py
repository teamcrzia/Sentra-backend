import os
from dotenv import load_dotenv

# 🔥 Load environment variables
load_dotenv()

class Config:
    # App settings
    DEBUG = True
    PORT = 5000

    # 🔐 API Keys
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

    # 🗄️ MongoDB Config
    MONGO_URI = os.getenv("MONGO_URI")
    DB_NAME = os.getenv("DB_NAME", "ai_chat_db")

    # ⚙️ Chat settings
    MAX_HISTORY = 5
    SUMMARY_TRIGGER = 5
    MAX_MESSAGE_LENGTH = 500
