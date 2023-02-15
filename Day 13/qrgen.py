from qr2022 import qrcode
import cv2
img=qrcode("HELLO NEPAL")
cv2.imshow("qr",img)
cv2.waitKey(0)