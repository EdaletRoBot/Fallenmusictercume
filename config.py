from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "23684473"))
API_HASH = getenv("API_HASH", "a2161b18cd38679ed40beed0d82f0b88")

BOT_TOKEN = getenv("BOT_TOKEN", "6119118831:AAEK2OsoMs-rb1oaSopzvvg-YlY1Hij7pDE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5540993505"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/9bbe79f7904d8e30053d7.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/9bbe79f7904d8e30053d7.jpg")

SESSION = getenv("SESSION", "AQCaZ9HbvXp2U54PviJgsPjROttd2bIejwyXlC1zcAgCnqOEw6ZCEe7P8kySWLo1NmhvXJqXPF1Bb0uses2PfWY9SM3pVZHwhgfVBlMUVmO9ZuwmiYOW7GVLMo6VsOFAJ6HIIt1HE0APGe7Cxj7vfg3bcEAfWK5DwFAomdsDEjonPGxOmVaP83HwMAtZWsR_93ArPQHB7NnHecVaNQXGYHCqqV8-APHRh_YJpfUd3SoCVTtDhrrzfkpL6E-mowQLMzggSNuDwsdzua-rJwX-9gc2s2IZimdd33dQPwW-7KYiXTGtt8IJhoIuN5kFTfjeBH549rwTN4MYOJsXyE0FNe4255wdgDcv7Lb6j4Sk6TZtmvFuL_jTi7Blq8qJcdFzJAAAAAVve29YA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/edaletsup")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/edaletproject")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5540993505").split()))


FAILED = "https://telegra.ph/file/9bbe79f7904d8e30053d7.jpg"
