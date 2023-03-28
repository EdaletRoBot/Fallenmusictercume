from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "24674105"))
API_HASH = getenv("API_HASH", "22db5eac13b6c972b6e87a9a0a33eb46")

BOT_TOKEN = getenv("BOT_TOKEN", "6286594190:AAFFUyRdGWZ5_b2APeaHjp-WPttqKN1dMHU")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6045596584"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/ce0c5d2a22e45cf39ad59.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/ce0c5d2a22e45cf39ad59.jpg")

SESSION = getenv("SESSION", "AQA8iTM3F3n7c0CSXq_1fUAv6XT3w1zciOxbhQGwxXu185gV_hBtj9Wh09OAWsB1jAJ33Him6CqGmNJD5mMuTVVyrLRzz_d8SmIO8LnNPS9-6HKAOV2DHZ3BZbd1913wUVVtCV8dkqU2QbPlfuTsBvf_otFevLoLSN3UyMfEc7gHqd4knN534iBJJZRWb_xVHauO2FwjgiXBafTm22JUDmtmB7gPepY8USbRTlaEIGPP2ZwzhJrT9r_cNVjlESqL_--sT0_KDi-NO72lgJUcBVta2SKbt7N7pgLRVv4Zem7RfxI9M3rTwBlBdHXXbuqqHpd2PchrMt9IG3YtvXHXt3SJAAAAAWGaX7EA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Sohbet_Region")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Sohbet_Region")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6045596584").split()))


FAILED = "https://telegra.ph/file/ce0c5d2a22e45cf39ad59.jpg"
