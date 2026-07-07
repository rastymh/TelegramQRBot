from datetime import datetime

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import ContextTypes


# 📢 Chat ID ـی چەنالەکەت
ADMIN_CHAT_ID = -1004418591711


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # ---------------- USER INFO ----------------
    user = update.effective_user

    first_name = user.first_name or "None"
    last_name = user.last_name if user.last_name else "None"
    username = f"@{user.username}" if user.username else "None"
    user_id = user.id
    language = user.language_code if user.language_code else "None"

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    admin_message = (
        "🆕 <b>New User Started The Bot</b>\n\n"
        f"👤 <b>First Name:</b> {first_name}\n"
        f"👥 <b>Last Name:</b> {last_name}\n"
        f"📛 <b>Username:</b> {username}\n"
        f"🆔 <b>User ID:</b> <code>{user_id}</code>\n"
        f"🌐 <b>Language:</b> {language}\n"
        f"🕒 <b>Date & Time:</b> {now}"
    )

    try:
        await context.bot.send_message(
            chat_id=ADMIN_CHAT_ID,
            text=admin_message,
            parse_mode="HTML",
        )
    except Exception as e:
        print(f"Notification Error: {e}")

    # ---------------- MENU ----------------
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
