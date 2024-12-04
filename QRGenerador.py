import qrcode
from PIL import Image, ImageDraw, ImageFilter
import cairosvg
import json

def make_rounded_qr_with_border(data, fill_color, back_color, logo, border_radius=20):
   
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGBA")
    qr_size = qr_img.size

    # Create a new image with rounded corners
    rounded_qr = Image.new("RGBA", qr_size, (255, 255, 255, 0))
    mask = Image.new("L", qr_size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle(
        (0, 0, qr_size[0], qr_size[1]), radius=border_radius, fill=255
    )
    rounded_qr.paste(qr_img, (0, 0), mask=mask)

    # Place the logo at the center
    if logo:
        logo_size = (qr_size[0] // 4, qr_size[1] // 4)
        logo = logo.resize(logo_size, Image.LANCZOS)
        logo = logo.convert("RGBA")
        # Create a new image white and rounded corners
        rounded_logo = Image.new("RGBA", logo_size, (255, 255, 255, 0))
        mask = Image.new("L", logo_size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle(
            (0, 0, logo_size[0], logo_size[1]), radius=border_radius, fill=255
        )
    
        pos = (
            (rounded_qr.size[0] - logo.size[0]) // 2,
            (rounded_qr.size[1] - logo.size[1]) // 2,
        )
        rounded_qr.paste(logo, pos, mask=logo)

    return rounded_qr


# Convert SVG logo to PNG
logo_path = 'logoAirFlow.svg'
output_logo = 'logo_modern.png'
cairosvg.svg2png(url=logo_path, write_to=output_logo, output_width=400, output_height=400)

# Load the logo
logo_image = Image.open(output_logo)

# Data for the QR code
data = {
    "uuid": "EPSG-GTI-PROY-3D",
    "num_serie": "ABC123456",
}

# Generate the QR code with rounded corners and integrated logo
rounded_qr_with_border = make_rounded_qr_with_border(
    data=json.dumps(data),
    fill_color="#52CCD7",
    back_color="white",
    logo=logo_image,
    border_radius=30,
)

# Save the output
output_file_with_border = f"QR_AirFlow_{data['uuid']}.png"
rounded_qr_with_border.save(output_file_with_border)

print(f"QR Code saved as: {output_file_with_border}")
