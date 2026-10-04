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
def fonk3(b5, b4):
    return b4.scan(b5)
def fonk4():
    b1 = fonk1()
    b4 = QR()
    while True:
        sleep(0.5)
        b5 = fonk2(b1)
        for f_x, f_y, data in fonk3(b5, b4):
            print(f_x, f_y, data)
if b6 = = "__main__":
    fonk4()