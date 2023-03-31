from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "21257388 "))
API_HASH = getenv("API_HASH", "26418a3017c92dca31d8b973f1f81018 ")

BOT_TOKEN = getenv("BOT_TOKEN", "5786085295:AAGxg4v-kCZbS0pB9wxy_dX2hKT1AZzyOCU")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5540993505"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/3b49e67c2e79d73923608.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/3b49e67c2e79d73923608.jpg")

SESSION = getenv("SESSION", "AQCaZ9HbvXp2U54PviJgsPjROttd2bIejwyXlC1zcHN7qNBZZa5SaIUqgoTPM2lFEc_M0vvdVTuHL8Mogxs8c_bsHkKdNh4TgufkuAyJdYTdfkohotgyp-O4ELzW2_Vs7ievvUtoifxhcV5JwqV330vAuwoabEbaIl-3_FAYZmqWwVk6ah9lkE-5BoNd9hIx6IyhWlnm50JymSUUvb89RZfKmEQ4f6Mubood40PvNps9QUSn39ZOE9MxUmaoXE9dVyP-59EgCKZM_fjSF1tupK6kFPioDiLNxtuzyQyIq2Q5-lPDfJOEq-zL6aNR31spEa0-Z3IrtLCEkjsWW__H_QigAAAAAUffa1cA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/edaletsup")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/edaletproject")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5540993505").split()))


FAILED = "https://telegra.ph/file/3b49e67c2e79d73923608.jpg"
