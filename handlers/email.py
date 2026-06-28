from telegram import Update
from telegram.ext import ContextTypes


async def email_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    context.user_data["type"] = "email"

    await query.message.reply_text(
        "📧 Email QR\n\n"
        "نموونە:\n"
        "example@gmail.com"
    )