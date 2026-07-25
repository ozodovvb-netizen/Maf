"""
Botning asosiy konfiguratsiyasi.
Barcha maxfiy ma'lumotlar (.env) faylidan o'qiladi.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# --- Bot sozlamalari ---
BOT_TOKEN = os.getenv("BOT_TOKEN", "PUT_YOUR_BOT_TOKEN_HERE")

# Botning o'zi ishlaydigan username (deep-link uchun, masalan https://t.me/Sherif_mafiabot)
BOT_USERNAME = os.getenv("BOT_USERNAME", "Sherif_mafiabot")

# --- Bosh adminlar (bot ishga tushganda avtomatik admin huquqiga ega bo'ladi) ---
# .env faylida: SUPER_ADMINS=123456789,987654321
SUPER_ADMINS = [
    int(x) for x in os.getenv("SUPER_ADMINS", "").split(",") if x.strip().isdigit()
]

# --- PostgreSQL ulanish satri ---
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://mafia_user:mafia_pass@localhost:5432/mafia_bot",
)

# --- O'yin sozlamalari ---
MIN_PLAYERS = int(os.getenv("MIN_PLAYERS", "5"))
MAX_PLAYERS = int(os.getenv("MAX_PLAYERS", "45"))

REGISTRATION_SECONDS = int(os.getenv("REGISTRATION_SECONDS", "90"))
NIGHT_SECONDS = int(os.getenv("NIGHT_SECONDS", "40"))
DAY_DISCUSSION_SECONDS = int(os.getenv("DAY_DISCUSSION_SECONDS", "60"))
VOTING_SECONDS = int(os.getenv("VOTING_SECONDS", "30"))
LAST_WORDS_SECONDS = int(os.getenv("LAST_WORDS_SECONDS", "30"))

# Kuniga nechta bepul "tasodifiy pul" so'rovi mumkin
FREE_MONEY_DAILY_LIMIT = int(os.getenv("FREE_MONEY_DAILY_LIMIT", "3"))

# Jinsni o'zgartirish limiti (umumiy, foydalanuvchi hisobida saqlanadi)
GENDER_CHANGE_LIMIT = int(os.getenv("GENDER_CHANGE_LIMIT", "3"))

# --- Qo'llab-quvvatlanadigan tillar ---
# Kod: (bayroq, nom) - tartib shu yerda ko'rsatilganidek chiqadi
LANGUAGES = {
    "uz": ("🇺🇿", "O'zbekcha"),
    "ru": ("🇷🇺", "Русский"),
    "en": ("🇺🇸", "English"),
    "ar": ("🇸🇦", "العربية"),
    "id": ("🇮🇩", "Indonesia"),
    "kk": ("🇰🇿", "Қазақша"),
    "tr": ("🇹🇷", "Türkçe"),
    "ko": ("🇰🇷", "한국어"),
}
DEFAULT_LANGUAGE = "uz"

# Faylni saqlash uchun papka (chek skrinshotlari, va h.k.)
MEDIA_STORAGE_CHANNEL_ID = int(os.getenv("MEDIA_STORAGE_CHANNEL_ID", "0"))  # ixtiyoriy
