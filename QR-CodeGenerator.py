import qrcode

qr = qrcode.make("Hello world")

qr.save("Meu_QRcode.png")

print("Qr code gerado com sucessor")
