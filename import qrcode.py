import qrcode
import webbrowser
import pyqrcode

# The Instagram account to generate a QR code for
account = 'estratekdata'

# The URL for the Instagram profile
url = f'https://www.instagram.com/{account}/'

# Generate the QR code as a PyQRCode object
qr = pyqrcode.create(url)

# Generate the QR code image as a PNG file
img_file = 'instagram_qr.png'
qr.png(img_file, scale=10)

# Open the QR code image in the default web browser
webbrowser.open(img_file, new = 1)