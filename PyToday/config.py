import os
import secrets
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb+srv://PythonToday:JXTg6cIx7tAhOJBk@cluster0.obhmjth.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7315481856:AAGmX1Ns-Jipm_OcE8WspU4no7o-JB610Ec")

ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY", "a7e5f2d8c9b1a0f3e4d2c8b7a6f5e1d3c9a8b7f6e5d4c3b2a1f0e9d8c7b6a5")
if not ENCRYPTION_KEY:
    ENCRYPTION_KEY = secrets.token_urlsafe(32)

ADMIN_USER_IDS = [int(x) for x in os.getenv("ADMIN_USER_IDS", "6510174019").split(",") if x.strip()]

SESSIONS_DIR = "sessions"
os.makedirs(SESSIONS_DIR, exist_ok=True)

BOT_USERNAME = os.getenv("BOT_USERNAME", "PyToday Adbot")
ACCOUNT_NAME_SUFFIX = os.getenv("ACCOUNT_NAME_SUFFIX", "PyAds")
ACCOUNT_BIO_TEMPLATE = os.getenv("ACCOUNT_BIO_TEMPLATE", "Smart Ads")

START_IMAGE_URL = os.getenv("START_IMAGE_URL", "https://i.ibb.co/p6mFW8JQ/file-3545.jpg")

ADMIN_ONLY_MODE = os.getenv("ADMIN_ONLY_MODE", "False").lower() == "true"

AUTO_REPLY_ENABLED = os.getenv("AUTO_REPLY_ENABLED", "False").lower() == "true"
AUTO_REPLY_TEXT = os.getenv("AUTO_REPLY_TEXT", "I'm currently unavailable. Go ahead and send your message, I will reply as soon as I can.")

AUTO_GROUP_JOIN_ENABLED = os.getenv("AUTO_GROUP_JOIN_ENABLED", "False").lower() == "true"

FORCE_SUB_CHANNEL = os.getenv("FORCE_SUB_CHANNEL", "")
FORCE_SUB_GROUP = os.getenv("FORCE_SUB_GROUP", "")
FORCE_SUB_ENABLED = os.getenv("FORCE_SUB_ENABLED", "False").lower() == "true"

SQLITE_DB_PATH = "bot_data.db"

CONNECTION_POOL_SIZE = 10
REQUEST_TIMEOUT = 30
MAX_RETRIES = 3
RETRY_DELAY = 5
