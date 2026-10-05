import cv2
import os
def fonk1():
    b1 = input("Enter the classifier name: ")
    b2 = os.path.join("images", b1)
    os.makedirs(b2, b3 = True)
    print("Folder created for:", b1)
    b4 = cv2.VideoCapture(0)
    b5 = cv2.VideoWriter_fourcc(*'XVID')
    b6 = cv2.VideoWriter('output.avi', b5, 20.0, (640, 480))
    while b4.isOpened():
        ret, b7 = b4.read()
        if ret:
            b7 = cv2.flip(b7, 1)
            b6.write(b7)
            cv2.imshow('b7', b7)
            if cv2.waitKey(1) & b8 = = ord('q'):
                break
        else:
            break
    b4.release()
    b6.release()
    cv2.destroyAllWindows()
    b9 = cv2.VideoCapture('output.avi')
    success, b10 = b9.read()
    a1 = 0
    while success:
        b11 = os.path.join("images", b1, f"b7{a1}.jpg")
        cv2.imwrite(b11, b10)
        print(f'Saved {b11}')
        success, b10 = b9.read()
        a1 += 1
if b12 = = "__main__":
    fonk1()