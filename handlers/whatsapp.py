from telegram import Update
from telegram.ext import ContextTypes

async def whatsapp_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    context.user_data["type"] = "whatsapp"

    await query.message.reply_text(
        "💬 WhatsApp QR\n\n+9647XXXXXXXX"
    )