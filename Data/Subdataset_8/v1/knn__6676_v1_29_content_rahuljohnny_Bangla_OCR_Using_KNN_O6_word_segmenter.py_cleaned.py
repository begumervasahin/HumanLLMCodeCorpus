import cv2
import numpy as np
import array
import os
def word_segmenter(count2):
    arr2 = []
    imgTestingNumbers2 = cv2.imread("words.png")
    if imgTestingNumbers2 is None:
        print("error: image not read from file \n\n")
        os.system("pause")
        return
    height, width, channels = imgTestingNumbers2.shape
    print("Height:")
    print(height)
    print("Width:")
    print(width)
    wordRatio = float(width) / float(height)
    print("Ratio:")
    print(wordRatio)
    if wordRatio >= 0.9:
        maxi = 9999
        inew0 = -999
        c = array.array('i', (0,) * 100)
        for i in range(0, int(height)
            for j in range(0, width):
                if np.any(imgTestingNumbers2[i, j] == 0):
                    c[i] = c[i] + 1
            if c[i] < maxi:
                maxi = c[i]
                inew = i
            elif c[i] - maxi <= int(width / 3):
                inew0 = i
        if inew0 > inew:
            irange = inew0
        else:
            irange = inew
        for i in range(inew - 2, irange + 2):
            for j in range(0, width):
                imgTestingNumbers2[i, j] = 1
    imgGray1 = cv2.cvtColor(imgTestingNumbers2, cv2.COLOR_BGR2GRAY)
    imgThresh1 = cv2.adaptiveThreshold(imgGray1,
                                       255,
                                       cv2.ADAPTIVE_THRESH_MEAN_C,
                                       cv2.THRESH_BINARY_INV,
                                       111,
                                       2
                                       )
    arr2.append(imgThresh1)
    if count2 == 1:
        cv2.imwrite("CreS2
    elif count2 == 3:
        cv2.imwrite("CreS2
    elif count2 == 2:
        cv2.imwrite("CreS2
    elif count2 == 4:
        cv2.imwrite("CreS2
    elif count2 == 5:
        cv2.imwrite("CreS2
    elif count2 == 6:
        cv2.imwrite("CreS2
    elif count2 == 7:
        cv2.imwrite("CreS2
    elif count2 == 8:
        cv2.imwrite("CreS2
    elif count2 == 9:
        cv2.imwrite("CreS2
    elif count2 == 10:
        cv2.imwrite("CreS2
    elif count2 == 0:
        cv2.imwrite("CreS2
    cv2.imwrite("wordseg.png", arr2[count2])
    cv2.imshow("shown", imgThresh1)
    cv2.waitKey(0)
    return imgThresh1
word_segmenter(1)
