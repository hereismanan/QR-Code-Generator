import qrcode as qr
img=qr.make("https://leetcode.com/u/hereismanan")
img.save("new_qr.png")