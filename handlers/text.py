from telegram import Update
from telegram.ext import ContextTypes

async def text_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    context.user_data["type"] = "text"

    await query.message.reply_text(
        "📝 Text QR\n\nهەر دەقێک بنێرە"
    )