from telegram import Update
from telegram.ext import ContextTypes


async def phone_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    context.user_data["type"] = "phone"

    await query.message.reply_text(
        "📞 Phone QR\n\n"
        "ژمارەی تەلەفۆن بنێرە:\n"
        "+9647712345678"
    )