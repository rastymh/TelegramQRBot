import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

LOGO_FOLDER = "assets/logos"
USER_LOGO_FOLDER = "assets/user_logo"
TEMP_FOLDER = "temp"