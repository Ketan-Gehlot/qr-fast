"""Generate the QR code image.
Usage:  python make_qr.py https://your-site-url/
Output: review_qr.png
"""
import sys
import qrcode

if len(sys.argv) < 2:
    sys.exit("Usage: python make_qr.py <URL where index.html is hosted>")

url = sys.argv[1]
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=20, border=4)
qr.add_data(url)
qr.make(fit=True)
qr.make_image(fill_color="black", back_color="white").save("review_qr.png")
print(f"Saved review_qr.png -> {url}")
