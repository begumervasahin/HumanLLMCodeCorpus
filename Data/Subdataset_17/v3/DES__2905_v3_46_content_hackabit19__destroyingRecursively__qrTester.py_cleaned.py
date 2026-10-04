from qr import QR
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
def initialize_camera():
    return PiCamera()
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
        qr_codes = scan_qr_codes(image, qr_scanner)
        for f_x, f_y, data in qr_codes:
            print(f"Coordinates: ({f_x}, {f_y}), Data: {data}")
if __name__ == "__main__":
    main()