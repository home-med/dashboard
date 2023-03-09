import segno
from PIL import Image
import tomllib

with open('config.toml', 'rb') as file:
    config = tomllib.load(file)


def make_qr(url, location, add_logo, output="qrcode.png") -> None:

    URL = url
    LOGO = config['INFO']['IMAGES']['img_folder'] + config['INFO']['IMAGES'][location]
    OUTPUT = output or "qrcode.png"
    if (OUTPUT != "qrcode.png" and len(OUTPUT.split(".")) == 1):
        OUTPUT += ".png"
        print(OUTPUT)
    # Make QR code
    qr = segno.make_qr(URL, error='H')
    qr.save(OUTPUT, scale=100, border=1)
    
    try:
        if (add_logo):
            # Now open that png image to put the logo
            img = Image.open(OUTPUT).convert("RGBA")

            width, height = img.size

            # How big the logo we want to put in the qr code png
            logo_size = int(width / 3)
            # Open the logo image
            logo = Image.open(LOGO).convert("RGBA")

            # Calculate xmin, ymin, xmax, ymax to put the logo
            xmin = ymin = int((width / 2) - (logo_size / 2))
            xmax = ymax = int((width / 2) + (logo_size / 2))

            # resize the logo as calculated
            logo = logo.resize((xmax - xmin, ymax - ymin))

            # put the logo in the qr code
            img.paste(logo, (xmin, ymin, xmax, ymax))

            img.save(OUTPUT)
    except FileNotFoundError:
        print("File not found.")
        pass