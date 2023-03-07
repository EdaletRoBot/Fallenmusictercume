from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "19485442"))
API_HASH = getenv("API_HASH", "a03fcb372b3ec4e406b5d52f84b02e53")

BOT_TOKEN = getenv("BOT_TOKEN", "5366398706:AAHMtMeafYqfqsvfFhZt3eBCdQsZFRGaH0k")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "571698989"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/ce0c5d2a22e45cf39ad59.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/ce0c5d2a22e45cf39ad59.jpg")

SESSION = getenv("SESSION", "AgAd64a2lrFnYr5PuTq1TT6kAhCefsr8zD9S8gIdO-iDCJTPUJ7DLFRo6W9pxuaUtXSd2bhjOWDxVM4V_UklsUM5WHGw28LNoKI3eYhdaeH17ho3qqCKf1bnWoBOWyVq6qsA4McIZpKmcBhVr4o8TcFD00z56yMFgW6SJBwmUYrPM_NatZag-CyBswq2assy4ebsfaQziQ7xF0h7Qh-U2hVajE1AeNr-vuJWKfb0xgStdo14LlT2zFjg_xWKD_3CwwG31OFG3WJqNfgn6Z2-dmiGHpIirnIPKhr2kVQ0qHSqMO8xJ2q-UhepOKdFpON4jaulVdpB8ToWYvi3afZ7DDRvAAAAAWV6XysA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/qruzdaa")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Cenublar")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5997485867").split()))


FAILED = "https://telegra.ph/file/ce0c5d2a22e45cf39ad59.jpg"
