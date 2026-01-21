import qrcode

data = input("Enter text or link for QR Code: ")

qr = qrcode.make(data)
qr.save("qr_code.png")

print("✅ QR Code generated successfully!")

