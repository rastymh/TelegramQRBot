from telegram import Update
from telegram.ext import ContextTypes

async def location_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    context.user_data["type"] = "location"

    await query.message.reply_text(
        "📍 Location QR\n\n"
        "Latitude,Longitude بنێرە\n"
        "Example: 36.1901,44.0090"
    )
    