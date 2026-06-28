from telegram import Update
from telegram.ext import ContextTypes

async def telegram_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    context.user_data["type"] = "telegram"

    await query.message.reply_text(
        "✈️ Telegram QR\n\n@username"
    )