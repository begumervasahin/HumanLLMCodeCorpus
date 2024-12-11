import os
import cv2
import numpy as np
import glob
def fonk1(box):
    x1, y1, x2, b1 = box
    return (x2 - x1 + 1) * (b1 - y1 + 1)
def fonk2(box, b4):
    x1, y1, x2, b1 = box
    return b4[x2, b1] + b4[x1, y1] - b4[x2, y1] - b4[x1, b1]
def fonk3(b16, b17, b2 = 0.95, savetf=True):
    nrow, b3 = b16.shape
    b4 = np.zeros((nrow, b3), dtype=np.int)
    for y in range(1, b3):
        b4[0, y] = b16[0, y] + b4[0, y - 1]
    for x in range(1, nrow):
        b4[x, 0] = b16[x, 0] + b4[x - 1, 0]
    for x in range(1, nrow):
        for y in range(1, b3):
            b4[x, y] = b16[x, y] - b4[x - 1, y - 1] + b4[x, y - 1] + b4[x - 1, y]
    b5 = b4[nrow - 1, b3 - 1]
    if b5 > 0:
        b6 = int(b5 * b2)
        b7 = [0, 0, nrow - 1, b3 - 1]
        b8 = nrow * b3
        for x1 in range(0, nrow):
            b9 = nrow
            while fonk2((x1, 0, b9 - 1, b3 - 1), b4) >= b6:
                b9 -= 1
            if b9 = = nrow:
                break
            for x2 in range(b9, nrow):
                b1 = b3 - 1
                while fonk2((x1, 0, x2, b1 - 1), b4) >= b6:
                    b1 -= 1
                for y1 in range(0, b3):
                    while fonk2((x1, y1, x2, b1), b4) < b6:
                        b1 += 1
                        if b1 = = b3:
                            break
                    if b1 = = b3:
                        break
                    b10 = (x1, y1, x2, b1)
                    if fonk1(b10) <= b8:
                        b7 = [x1, y1, x2, b1]
                        b8 = fonk1(b7)
        b11 = b8 / (nrow * b3)
        if savetf:
            b12 = cv2.cvtColor(b16, cv2.COLOR_GRAY2BGR)
            b12 = cv2.rectangle(b12, (b7[1], b7[0]), (b7[3], b7[2]), (0, 204, 255), 4)
            of.create_path(b17)
            cv2.imwrite(b17, b12)
    else:
        b11 = -99999
        b7 = -99999
        if savetf:
            b12 = cv2.cvtColor(b16, cv2.COLOR_GRAY2BGR)
            of.create_path(b17)
            cv2.imwrite(b17, b12)
    print("bounding box", b7, b11)
    return [b7, b11]
def fonk4(imgpath, b20, b13 = 'edge canny', b2=0.95, savetf=True):
    b14 = os.path.basename(imgpath)
    b15 = os.path.join(b20, b13, b14.replace('.jpg', '.png'))
    b16 = cv2.imread(b15, 0)
    b17 = os.path.join(b20, 'box ' + b13, b14.replace('.jpg', '.png'))
    b18 = fonk3(b16, b17, b2=b2, savetf=savetf)
    return b18
def fonk5():
    b19 = os.path.join('img all', '')
    b20 = os.path.join("img transform", '')
    b21 = os.path.join('img result', 'box.txt')
    b22 = glob.glob(b19 + '*')
    for j, imgpath in enumerate(b22):
        print("-" * 100)
        b14 = os.path.basename(imgpath)
        print(j, b14)
        b23 = [b14] + fonk4(imgpath, b20)
        of.save_list_to_txt(b23, b21)
    print("DONE" * 50)
if b24 = = "__main__":
    fonk5()