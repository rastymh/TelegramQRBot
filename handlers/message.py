from telegram import Update
from telegram.ext import ContextTypes
from services.qr_generator import create_qr


LOGO_MAP = {
    "website": "assets/logos/website.png",
    "wifi": "assets/logos/wifi.png",
    "phone": "assets/logos/phone.png",
    "email": "assets/logos/email.png",
    "text": "assets/logos/text.png",
    "whatsapp": "assets/logos/whatsapp.png",
    "telegram": "assets/logos/telegram.png",
    "facebook": "assets/logos/facebook.png",
    "instagram": "assets/logos/instagram.png",
    "location": "assets/logos/location.png",
}


def build_qr_data(user_type, text):

    if user_type == "wifi":
        ssid, password = "", ""
        for line in text.split("\n"):
            if line.startswith("SSID:"):
                ssid = line.replace("SSID:", "").strip()
            elif line.startswith("PASSWORD:"):
                password = line.replace("PASSWORD:", "").strip()
        return f"WIFI:T:WPA;S:{ssid};P:{password};;"

    elif user_type == "phone":
        return f"tel:{text}"

    elif user_type == "email":
        return f"mailto:{text}"

    elif user_type == "whatsapp":
        return f"https://wa.me/{text.replace('+','')}"

    elif user_type == "telegram":
        return f"https://t.me/{text.replace('@','')}"

    elif user_type == "location":
        return f"https://maps.google.com/?q={text}"

    else:
        return text


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message or not update.message.text:
        return

    text = update.message.text

    if text.startswith("/"):
        return

    user_type = context.user_data.get("type", "website")

    qr_data = build_qr_data(user_type, text)

    logo_path = context.user_data.get("custom_logo") or LOGO_MAP.get(
        user_type,
        "assets/logos/website.png"
    )

    buffer = create_qr(qr_data, logo_path)

    await update.message.reply_photo(
        photo=buffer,
        caption=f"✅ {user_type.upper()} QR Code ـەکەت ئامادەیە"
    )