import cv2
import os
def fonk1():
    b1 = input("Enter the classifier name: ")
    b2 = "images/" + b1
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
        cv2.imwrite(f'images/{b1}/b7{a1}.jpg', b10)
        print('Saved b7%d.jpg' % a1)
        success, b10 = b9.read()
        a1 += 1
if b11 = = "__main__":
    fonk1()