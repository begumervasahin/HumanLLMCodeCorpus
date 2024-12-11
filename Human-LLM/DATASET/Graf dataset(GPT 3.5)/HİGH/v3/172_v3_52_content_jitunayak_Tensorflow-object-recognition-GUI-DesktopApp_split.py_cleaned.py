import cv2
import os
def fonk1(b8):
    b1 = os.path.join("images", b8)
    os.makedirs(b1, b2 = True)
    print("Folder created for:", b8)
    return b1
def fonk2(b8):
    b3 = cv2.VideoCapture(0)
    b4 = cv2.VideoWriter_fourcc(*'XVID')
    b5 = cv2.VideoWriter('output.avi', b4, 20.0, (640, 480))
    a1 = 0
    while b3.isOpened():
        ret, b6 = b3.read()
        if ret:
            b6 = cv2.flip(b6, 1)
            b5.write(b6)
            cv2.imshow('b6', b6)
            if cv2.waitKey(1) & b7 = = ord('q'):
                break
            cv2.imwrite(f'images/{b8}/b6{a1}.jpg', b6)
            print(f'Saved b6{a1}.jpg')
            a1 += 1
        else:
            break
    b3.release()
    b5.release()
    cv2.destroyAllWindows()
def fonk3():
    b8 = input("Enter the classifier name: ")
    b9 = fonk1(b8)
    fonk2(b8)
if b10 = = "__main__":
    fonk3()