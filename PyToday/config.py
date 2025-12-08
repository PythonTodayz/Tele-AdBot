import os
import secrets
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY", "")
if not ENCRYPTION_KEY:
    ENCRYPTION_KEY = secrets.token_urlsafe(32)
    print("WARNING: ENCRYPTION_KEY not set. Generated a random key for this session.")
    print("For production, please set ENCRYPTION_KEY environment variable.")

ADMIN_USER_IDS = [int(x) for x in os.getenv("ADMIN_USER_IDS", "7756391784").split(",") if x.strip()]

SESSIONS_DIR = "sessions"
os.makedirs(SESSIONS_DIR, exist_ok=True)

BOT_USERNAME = os.getenv("BOT_USERNAME", "PyToday Adbot")
ACCOUNT_NAME_SUFFIX = os.getenv("ACCOUNT_NAME_SUFFIX", "- PyToday Ads")
ACCOUNT_BIO_TEMPLATE = os.getenv("ACCOUNT_BIO_TEMPLATE", "Adbot by @dojutso | Bot @PyTodayAdsBot")

START_IMAGE_URL = "https://i.ibb.co/p6mFW8JQ/file-3545.jpg"

ADMIN_ONLY_MODE = os.getenv("ADMIN_ONLY_MODE", "False").lower() == "true"

AUTO_REPLY_ENABLED = os.getenv("AUTO_REPLY_ENABLED", "False").lower() == "true"
AUTO_REPLY_TEXT = os.getenv("AUTO_REPLY_TEXT", "Abhi main offline hu. Tum apna text likhdo main jald se jald reply dene ki koshish karunga.")

AUTO_GROUP_JOIN_ENABLED = os.getenv("AUTO_GROUP_JOIN_ENABLED", "False").lower() == "true"
