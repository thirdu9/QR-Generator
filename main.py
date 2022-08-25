import qrcode as qr

def simple_qr(text):
    img = qr.make(text)
    img.save("simple_qr.png")

def colored_qr():
    pass

text = input('Enter text: ')
simple_qr(text)