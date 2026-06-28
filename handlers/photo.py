import os
from telegram import Update
from telegram.ext import ContextTypes

LOGO_PATH = "assets/user_logo/custom.png"


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.user_data.get("awaiting_logo"):
        return

    photo = update.message.photo[-1]
    file = await photo.get_file()

    os.makedirs("assets/user_logo", exist_ok=True)

    await file.download_to_drive(LOGO_PATH)

    context.user_data["custom_logo"] = LOGO_PATH
    context.user_data["awaiting_logo"] = False

    await update.message.reply_text("✅ لۆگۆکەت upload کرا!")