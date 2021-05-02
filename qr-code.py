import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://youtu.be/pVHKp6ffURY')
qr.make(fit=True)

img = qr.make_image(fill_color="orange", back_color="black")

file = "myrusakov_out_1.png"
img.save(file)