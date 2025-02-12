import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
YANDEX_TOKEN = os.getenv("YANDEX_TOKEN")
ALLOWED_USERS = list(map(int, os.getenv("ALLOWED_IDS").split(",")))
YANDEX_FOLDER = os.getenv("YANDEX_FOLDER")