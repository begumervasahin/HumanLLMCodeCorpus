import cv2
import os
from PIL import Image
base = "C:/melfaiz/eigenfaces/faces"
def new_face(name, path):
    path = os.path.join(base, path)
    os.makedirs(path, exist_ok=True)
    os.chdir(path)
    cam = cv2.VideoCapture(0)
    img_counter = 0
    images = []
    shape = (100, 100)
    face_cascade = cv2.CascadeClassifier("C:/melfaiz/eigenfaces/haarcascade_frontalface_alt.xml")
    while True:
        ret, frame = cam.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, f"Capture {img_counter}", (240, 50), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
        face_detect = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in face_detect:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            crop_img = frame[y + 2:y + h - 2, x + 2:x + w - 2]
            crop_img = cv2.resize(crop_img, shape)
        cv2.imshow("Training", frame)
        k = cv2.waitKey(1)
        if k % 256 == 27 or cv2.getWindowProperty('Training', 0) < 0:
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            img_name = f"opencv_frame_{img_counter}.png"
            images.append(crop_img)
            title = f"{name}_{img_counter}.png"
            cv2.imwrite(title, crop_img)
            img_counter += 1
    cam.release()
    cv2.destroyAllWindows()