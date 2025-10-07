import qrcode

content = input("Enter the QR Code Code content: ").strip()
filename = input("Enter the file name to save the QR Code: ").strip()

img = qrcode.make(content)
type(img)
img.save(filename+".png")
print("QR Code saved to "+filename+".png")