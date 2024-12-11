from importer import *
b1 = []
def fonk1(b10):
    b2 = cv2.imread("words.png")
    if b2 is None:
        print("error: image not read from file \n\n")
        os.system("pause")
        return
    height, width, b3 = b2.shape
    print("Height:")
    print(height)
    print("Width:")
    print(width)
    b4 = float(width) / float(height)
    print("Ratio:")
    print(b4)
    if b4 >= 0.9:
        a1 = 9999
        a2 = -999
        b5 = array.array('i', (0,) * 100)
        for i in range(0, int(height) / 2):
            for j in range(0, width):
                if np.any(b2[i, j] == 0):
                    b5[i] = b5[i] + 1
            if b5[i] < a1:
                a1 = b5[i]
                b6 = i
            elif b5[i] - a1 <= int(width / 3):
                a2 = i
        if a2 > b6:
            b7 = a2
        else:
            b7 = b6
        for i in range(b6 - 2, b7 + 2):
            for j in range(0, width):
                b2[i, j] = 1
    b8 = cv2.cvtColor(b2, cv2.COLOR_BGR2GRAY)
    b9 = cv2.adaptiveThreshold(b8, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 111, 2)
    b1.append(b9)
    if b10 = = 1:
        cv2.imwrite("CreS2
    elif b10 = = 3:
        cv2.imwrite("CreS2
    elif b10 = = 2:
        cv2.imwrite("CreS2
    elif b10 = = 4:
        cv2.imwrite("CreS2
    elif b10 = = 5:
        cv2.imwrite("CreS2
    elif b10 = = 6:
        cv2.imwrite("CreS2
    elif b10 = = 7:
        cv2.imwrite("CreS2
    elif b10 = = 8:
        cv2.imwrite("CreS2
    elif b10 = = 9:
        cv2.imwrite("CreS2
    elif b10 = = 10:
        cv2.imwrite("CreS2
    elif b10 = = 0:
        cv2.imwrite("CreS2
    cv2.imwrite("wordseg.png", b1[b10])
    cv2.imshow("shown", b9)
    cv2.waitKey(0)
    return b9