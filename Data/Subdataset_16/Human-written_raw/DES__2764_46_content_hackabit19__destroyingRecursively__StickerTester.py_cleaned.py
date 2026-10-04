from Sticker import Sticker
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import cv2
b1 = PiCamera()
b2 = Sticker()
while True:
    sleep(0.5)
    b3 = PiRGBArray(b1)
    b1.capture(b3, b4 = "bgr")
    b5 = b3.array
    found, x, b6 = b2.find_sticker(b5, True)
    print(found)