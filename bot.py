import os
import threading

from flask import Flask
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)

from config import BOT_TOKEN
from handlers.start import start
from handlers.menu import handle_menu
from handlers.message import handle_message
from handlers.photo import handle_photo

# ---------- Flask ----------
web = Flask(__name__)

@web.route("/")
def home():
    return "Telegram QR Bot is running!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    web.run(host="0.0.0.0", port=port)

# ---------- Telegram ----------
def main():
    threading.Thread(target=run_web, daemon=True).start()

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_menu))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    print("🤖 Bot is running...")

    app.run_polling()

if __name__ == "__main__":
    main()
