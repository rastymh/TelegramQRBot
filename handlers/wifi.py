from telegram import Update
from telegram.ext import ContextTypes


async def wifi_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    context.user_data["type"] = "wifi"

    await query.message.reply_text(
        "📶 WiFi QR\n\n"
        "ئێستا ئەم زانیاریانە بنێرە بە ئەم شێوەیە:\n\n"
        "SSID:YourWifiName\n"
        "PASSWORD:YourPassword"
    )