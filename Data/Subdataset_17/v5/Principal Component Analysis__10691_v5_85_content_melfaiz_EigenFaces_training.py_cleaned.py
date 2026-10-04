import cv2
import os
from PIL import Image
BASE_DIR = "C:/melfaiz/eigenfaces/faces"
def initialize_directory(path):
    os.makedirs(path, exist_ok=True)
    os.chdir(path)
def capture_images(name, path):
    full_path = os.path.join(BASE_DIR, path)
    initialize_directory(full_path)
    cam = cv2.VideoCapture(0)
    img_counter = 0
    shape = (100, 100)
    face_cascade = cv2.CascadeClassifier("C:/melfaiz/eigenfaces/haarcascade_frontalface_alt.xml")
    while True:
        ret, frame = cam.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        display_capture_counter(frame, img_counter)
        face_detect = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in face_detect:
            draw_face_rectangle(frame, x, y, w, h)
            crop_img = crop_and_resize_face(frame, x, y, w, h, shape)
        cv2.imshow("Training", frame)
        if handle_key_events(cam, frame, name, img_counter, crop_img):
            break
        img_counter += 1
    cam.release()
    cv2.destroyAllWindows()
def display_capture_counter(frame, img_counter):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, f"Capture {img_counter}", (240, 50), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
def draw_face_rectangle(frame, x, y, w, h):
    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
def crop_and_resize_face(frame, x, y, w, h, shape):
    crop_img = frame[y + 2:y + h - 2, x + 2:x + w - 2]
    return cv2.resize(crop_img, shape)
def handle_key_events(cam, frame, name, img_counter, crop_img):
    k = cv2.waitKey(1)
    if k % 256 == 27 or cv2.getWindowProperty('Training', 0) < 0:
        print("Escape hit, closing...")
        return True
    elif k % 256 == 32:
        save_captured_image(name, img_counter, crop_img)
    return False
def save_captured_image(name, img_counter, crop_img):
    img_name = f"{name}_{img_counter}.png"
    cv2.imwrite(img_name, crop_img)
