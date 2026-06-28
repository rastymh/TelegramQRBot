import qrcode
from PIL import Image
from io import BytesIO


def create_qr(data: str, logo_path: str = None):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # 👉 add logo if exists
    if logo_path:
        logo = Image.open(logo_path)

        base_width = 80
        logo = logo.resize((base_width, base_width))

        pos = (
            (img.size[0] - logo.size[0]) // 2,
            (img.size[1] - logo.size[1]) // 2
        )

        img.paste(logo, pos)

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer