import cv2
import os
b1 = "b14/"
b2 = "b8/"
def fonk1(image_path):
    b3 = "haarcascade_frontalface_alt.xml"
    b4 = cv2.CascadeClassifier(b3)
    b5 = cv2.imread(image_path)
    if b5 is None:
        print(f"Could not read image: {image_path}")
        return
    try:
        b6 = (b5.shape[1], b5.shape[0])
        b7 = cv2.resize(b5, b6)
        b8 = b4.detectMultiScale(b7)
        for f in b8:
            x, y, w, b9 = [v for v in f]
            cv2.rectangle(b5, (x, y), (x + w, y + b9), (0, 255, 0), 2)
            b10 = b5[y:y + b9, x:x + w]
            b11 = os.path.basename(image_path)
            b12 = os.path.join(b2, b11)
            cv2.imwrite(b12, b10)
            print(f"Writing: {b12}")
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
if b13 = = '__main__':
    if not os.path.exists(b2):
        os.makedirs(b2)
    b14 = os.listdir(b1)
    for i, b5 in enumerate(b14):
        b15 = os.path.join(b1, b5)
        print(f"Processing {i + 1}/{len(b14)}: {b5}")
        fonk1(b15)