from qr import QR
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import cv2
def fonk1():
    b1 = PiCamera()
    return b1
def fonk2(b1):
    b2 = PiRGBArray(b1)
    b1.capture(b2, b3 = "bgr")
    return b2.array
def fonk3(b6, b5):
    b4 = b5.scan(b6)
    for f_x, f_y, data in b4:
        print(f"Coordinates: ({f_x}, {f_y}), Data: {data}")
def fonk4():
    b1 = fonk1()
    b5 = QR()
    while True:
        sleep(0.5)
        b6 = fonk2(b1)
        fonk3(b6, b5)
if b7 = = "__main__":
    fonk4()