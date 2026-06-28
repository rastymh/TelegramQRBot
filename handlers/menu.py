from handlers.website import website_menu
from handlers.wifi import wifi_menu
from handlers.phone import phone_menu
from handlers.email import email_menu
from handlers.text import text_menu
from handlers.whatsapp import whatsapp_menu
from handlers.telegram import telegram_menu
from handlers.facebook import facebook_menu
from handlers.instagram import instagram_menu
from handlers.location import location_menu


async def handle_menu(update, context):
    query = update.callback_query
    data = query.data

    context.user_data["type"] = data

    # 👉 enable logo upload mode
    context.user_data["awaiting_logo"] = True

    await query.answer()

    if data == "website":
        await website_menu(update, context)

    elif data == "wifi":
        await wifi_menu(update, context)

    elif data == "phone":
        await phone_menu(update, context)

    elif data == "email":
        await email_menu(update, context)

    elif data == "text":
        await text_menu(update, context)

    elif data == "whatsapp":
        await whatsapp_menu(update, context)

    elif data == "telegram":
        await telegram_menu(update, context)

    elif data == "facebook":
        await facebook_menu(update, context)

    elif data == "instagram":
        await instagram_menu(update, context)

    elif data == "location":
        await location_menu(update, context)

    await query.message.reply_text(
        "🖼 تکایە لۆگۆی QR Code بنێرە (photo upload)"
    )