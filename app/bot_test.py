import os
from dotenv import load_dotenv
from telegram import Bot

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')

if not TOKEN or not ADMIN_ID:
    print('Please set BOT_TOKEN and ADMIN_ID in .env')
    raise SystemExit(1)

bot = Bot(token=TOKEN)
bot.send_message(chat_id=int(ADMIN_ID), text='✅ Тест: бот подключён и рабочий.')
print('Message sent.')