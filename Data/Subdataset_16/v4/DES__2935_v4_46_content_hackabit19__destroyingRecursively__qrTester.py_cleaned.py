from qr import QR
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import cv2
def fonk1():
    return PiCamera()
def fonk2(b4):
    b1 = PiRGBArray(b4)
    b4.capture(b1, b2 = "bgr")
    return b1.array
def fonk3(b6, b5):
    b3 = b5.scan(b6)
    for f_x, f_y, data in b3:
        print(f"Coordinates: ({f_x}, {f_y}), Data: {data}")
def fonk4():
    b4 = fonk1()
    b5 = QR()
    while True:
        sleep(0.5)
        b6 = fonk2(b4)
        fonk3(b6, b5)
if b7 = = "__main__":
    fonk4()