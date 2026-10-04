import cv2
import os
b1 = "images/"
b2 = "b8/"
def fonk1(b14):
    b3 = "haarcascade_frontalface_alt.xml"
    b4 = cv2.CascadeClassifier(b3)
    b5 = cv2.imread(b14)
    if b5 is None:
        print(f"Could not read b5: {b14}")
        return
    try:
        b6 = (b5.shape[1], b5.shape[0])
        b7 = cv2.resize(b5, b6)
        b8 = b4.detectMultiScale(b7)
        for (x, y, w, h) in b8:
            cv2.rectangle(b5, (x, y), (x + w, y + h), (0, 255, 0), 2)
            b9 = b5[y:y + h, x:x + w]
            b10 = os.path.basename(b14)
            b11 = os.path.join(b2, b10)
            cv2.imwrite(b11, b9)
            print(f"Saved cropped face to: {b11}")
    except Exception as e:
        print(f"Error processing b5 {b14}: {e}")
if b12 = = '__main__':
    if not os.path.exists(b2):
        os.makedirs(b2)
    b13 = os.listdir(b1)
    for index, image_file in enumerate(b13):
        b14 = os.path.join(b1, image_file)
        print(f"Processing {index + 1}/{len(b13)}: {image_file}")
        fonk1(b14)