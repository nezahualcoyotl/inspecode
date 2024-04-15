import qrcode
from PIL import Image, ImageDraw

input = 'Esto es un ejemplo'
'''qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Esto es un ejemplo del codigo QR')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('ejemplo1.png')'''


'''img = Image.new('RGB', (500, 400))

d = ImageDraw.Draw(img)
d.text((250, 200), "ROROLAS.PY", fill=(155, 155, 150))

img.save('imagen con texto.png')'''

img = Image.new('RGB', (500, 400), color=(255,255,255))

d = ImageDraw.Draw(img)
d.text((250, 200), "ROROLAS.PY", fill=(0,0,0))

img.save('imagen con texto.png')