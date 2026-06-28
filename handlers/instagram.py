from telegram import Update
from telegram.ext import ContextTypes

async def instagram_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    context.user_data["type"] = "instagram"

    await query.message.reply_text(
        "📸 Instagram QR\n\nhttps://instagram.com/username"
    )
    