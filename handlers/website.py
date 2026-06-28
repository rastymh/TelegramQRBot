from telegram import Update
from telegram.ext import ContextTypes


async def website_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    await query.answer()

    await query.message.reply_text(
        "🌐 تکایە لینکی وێبسایت بنێرە\n"
        "بۆ نموونە:\n"
        "https://example.com"
    )