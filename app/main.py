import os
import asyncio
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from fetcher import fetcher_loop
from notifier import Notifier

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")
UPDATE_INTERVAL = int(os.getenv("UPDATE_INTERVAL", "60"))

if not TOKEN or not ADMIN_ID:
    raise SystemExit("Please set BOT_TOKEN and ADMIN_ID in .env or environment variables.")

# Basic bot handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Бот ставок активен. Я буду присылать сигналы в этот чат.")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот работает. Я буду мониторить линии и присылать сигналы.")

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Остановка не реализована в макете.")

async def background_task(app):
    notifier = Notifier(app.bot, int(ADMIN_ID))
    await fetcher_loop(notifier, update_interval=UPDATE_INTERVAL)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("stop", stop))
    loop = asyncio.get_event_loop()
    loop.create_task(background_task(app))
    print("Bot started. Listening for commands...")
    app.run_polling()

if __name__ == '__main__':
    main()
