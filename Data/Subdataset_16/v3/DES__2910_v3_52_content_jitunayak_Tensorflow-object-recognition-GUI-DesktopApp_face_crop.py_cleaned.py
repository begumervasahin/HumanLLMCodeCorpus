import cv2
import os
b1 = "images/"
b2 = "b6/"
def fonk1(b11):
    b3 = "haarcascade_frontalface_alt.xml"
    b4 = cv2.CascadeClassifier(b3)
    b5 = cv2.imread(b11)
    if b5 is None:
        print(f"Could not read b5: {b11}")
        return
    try:
        b6 = b4.detectMultiScale(b5)
        for (x, y, w, h) in b6:
            b7 = b5[y:y + h, x:x + w]
            b8 = os.path.basename(b11)
            b9 = os.path.join(b2, b8)
            cv2.imwrite(b9, b7)
            print(f"Saved cropped face to: {b9}")
    except Exception as e:
        print(f"Error processing b5 {b11}: {e}")
def fonk2(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
def fonk3():
    fonk2(b2)
    b10 = os.listdir(b1)
    for index, image_file in enumerate(b10):
        b11 = os.path.join(b1, image_file)
        print(f"Processing {index + 1}/{len(b10)}: {image_file}")
        fonk1(b11)
if b12 = = '__main__':
    fonk3()