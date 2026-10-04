from Sticker import Sticker
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import cv2
def initialize_camera():
    return PiCamera()
def capture_image(camera):
    raw_capture = PiRGBArray(camera)
    camera.capture(raw_capture, format="bgr")
    return raw_capture.array
def find_and_print_sticker(image, sticker_detector):
    found, x, y = sticker_detector.find_sticker(image, True)
    if found:
        print(f"Sticker found at coordinates: ({x}, {y})")
    else:
        print("Sticker not found")
def main():
    camera = initialize_camera()
    sticker_detector = Sticker()
    while True:
        sleep(0.5)
        image = capture_image(camera)
        find_and_print_sticker(image, sticker_detector)
if __name__ == "__main__":
    main()