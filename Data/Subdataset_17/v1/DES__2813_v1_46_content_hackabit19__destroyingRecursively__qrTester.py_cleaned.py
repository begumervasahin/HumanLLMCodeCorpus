from qr import QR
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import cv2
def initialize_camera():
    camera = PiCamera()
    return camera
def capture_image(camera):
    raw_capture = PiRGBArray(camera)
    camera.capture(raw_capture, format="bgr")
    return raw_capture.array
def scan_qr_codes(image, qr_scanner):
    return qr_scanner.scan(image)
def main():
    camera = initialize_camera()
    qr_scanner = QR()
    while True:
        sleep(0.5)
        image = capture_image(camera)
        for f_x, f_y, data in scan_qr_codes(image, qr_scanner):
            print(f_x, f_y, data)
if __name__ == "__main__":
    main()