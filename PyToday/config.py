import os
import secrets
from dotenv import load_dotenv

load_dotenv()

# MongoDB Configuration
MONGODB_URI = os.getenv("MONGODB_URI", "")

# Bot Configuration
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# Encryption Key
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY", "")
if not ENCRYPTION_KEY:
    ENCRYPTION_KEY = secrets.token_urlsafe(32)

# Admin Configuration
ADMIN_USER_IDS = [int(x) for x in os.getenv("ADMIN_USER_IDS", "").split(",") if x.strip()]

# Sessions Directory
SESSIONS_DIR = "sessions"
os.makedirs(SESSIONS_DIR, exist_ok=True)

# Bot Info
BOT_USERNAME = os.getenv("BOT_USERNAME", "")
ACCOUNT_NAME_SUFFIX = os.getenv("ACCOUNT_NAME_SUFFIX", "")
ACCOUNT_BIO_TEMPLATE = os.getenv("ACCOUNT_BIO_TEMPLATE", "")

# Media
START_IMAGE_URL = os.getenv("START_IMAGE_URL", "")

# Admin Only Mode
ADMIN_ONLY_MODE = os.getenv("ADMIN_ONLY_MODE", "False").lower() == "true"

# Auto Reply Configuration
AUTO_REPLY_ENABLED = os.getenv("AUTO_REPLY_ENABLED", "False").lower() == "true"
AUTO_REPLY_TEXT = os.getenv("AUTO_REPLY_TEXT", "")

# Auto Group Join Configuration
AUTO_GROUP_JOIN_ENABLED = os.getenv("AUTO_GROUP_JOIN_ENABLED", "False").lower() == "true"

# Force Subscribe Configuration (Using IDs instead of links)
FORCE_SUB_ENABLED = os.getenv("FORCE_SUB_ENABLED", "False").lower() == "true"
FORCE_SUB_CHANNEL_ID = os.getenv("FORCE_SUB_CHANNEL_ID", "")  # Channel ID (e.g., -1001234567890)
FORCE_SUB_GROUP_ID = os.getenv("FORCE_SUB_GROUP_ID", "")  # Group ID (e.g., -1001234567890)

# Logs Channel Configuration
LOGS_CHANNEL_ID = os.getenv("LOGS_CHANNEL_ID", "")  # Channel ID for logs (e.g., -1001234567890)

# Database
SQLITE_DB_PATH = os.getenv("SQLITE_DB_PATH", "bot_data.db")

# Connection Settings
CONNECTION_POOL_SIZE = int(os.getenv("CONNECTION_POOL_SIZE", "10"))
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "30"))
MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))
RETRY_DELAY = int(os.getenv("RETRY_DELAY", "5"))

# Group Links File - Auto-detect path
import os as _os
_script_dir = _os.path.dirname(_os.path.abspath(__file__))
_default_group_file = _os.path.join(_script_dir, '..', 'group_mps.txt')
if not _os.path.exists(_default_group_file):
    _default_group_file = 'group_mps.txt'
GROUP_LINKS_FILE = os.getenv("GROUP_LINKS_FILE", _default_group_file)
