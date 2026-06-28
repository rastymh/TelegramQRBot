from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton("🌐 Website", callback_data="website"),
            InlineKeyboardButton("📶 WiFi", callback_data="wifi"),
        ],
        [
            InlineKeyboardButton("📞 Phone", callback_data="phone"),
            InlineKeyboardButton("📧 Email", callback_data="email"),
        ],
        [
            InlineKeyboardButton("📝 Text", callback_data="text"),
            InlineKeyboardButton("💬 WhatsApp", callback_data="whatsapp"),
        ],
        [
            InlineKeyboardButton("✈️ Telegram", callback_data="telegram"),
            InlineKeyboardButton("📘 Facebook", callback_data="facebook"),
        ],
        [
            InlineKeyboardButton("📸 Instagram", callback_data="instagram"),
            InlineKeyboardButton("📍 Location", callback_data="location"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 بەخێربێیت بۆ QR Code Generator\n\n"
        "تکایە جۆری QR Code هەڵبژێرە:",
        reply_markup=reply_markup,
    )