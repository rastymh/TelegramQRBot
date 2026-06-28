from telegram import Update
from telegram.ext import ContextTypes

async def facebook_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    context.user_data["type"] = "facebook"

    await query.message.reply_text(
        "📘 Facebook QR\n\nhttps://facebook.com/username"
    )