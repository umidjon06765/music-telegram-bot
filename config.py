import os
from dotenv import load_dotenv

# .env faylni yuklash
load_dotenv()

# Token va Spotify ma'lumotlarini olish
BOT_TOKEN = os.getenv("BOT_TOKEN")
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")


