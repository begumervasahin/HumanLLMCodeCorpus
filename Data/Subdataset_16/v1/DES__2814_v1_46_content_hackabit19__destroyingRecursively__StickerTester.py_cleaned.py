from Sticker import Sticker
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
    found, x, b4 = b5.find_sticker(b6, True)
    print(f"Sticker found: {found}, Coordinates: ({x}, {b4})")
def fonk4():
    b1 = fonk1()
    b5 = Sticker()
    while True:
        sleep(0.5)
        b6 = fonk2(b1)
        fonk3(b6, b5)
if b7 = = "__main__":
    fonk4()