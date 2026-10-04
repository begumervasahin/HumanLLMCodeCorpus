from Sticker import Sticker
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
    found, x, b3 = b5.find_sticker(b6, draw=True)
    if found:
        print(f"Sticker found at coordinates: ({x}, {b3})")
    else:
        print("Sticker not found")
def fonk4():
    b4 = fonk1()
    b5 = Sticker()
    while True:
        sleep(0.5)
        b6 = fonk2(b4)
        fonk3(b6, b5)
if b7 = = "__main__":
    fonk4()