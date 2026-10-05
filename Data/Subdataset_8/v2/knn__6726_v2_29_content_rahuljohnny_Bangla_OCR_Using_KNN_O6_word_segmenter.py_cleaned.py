import cv2
import numpy as np
import os
def word_segmenter(count):
    arr = []
    imgTestingNumbers = cv2.imread("words.png")
    if imgTestingNumbers is None:
        print("Error: image not read from file")
        return
    height, width, _ = imgTestingNumbers.shape
    print("Height:", height)
    print("Width:", width)
    word_ratio = width / height
    print("Ratio:", word_ratio)
    if word_ratio >= 0.9:
        maxi = 9999
        inew = -999
        c = np.zeros(100, dtype=int)
        for i in range(height
            for j in range(width):
                if np.any(imgTestingNumbers[i, j] == 0):
                    c[i] += 1
            if c[i] < maxi:
                maxi = c[i]
                inew = i
            elif c[i] - maxi <= width / 3:
                inew0 = i
        if inew0 > inew:
            irange = inew0
        else:
            irange = inew
        for i in range(inew - 2, irange + 2):
            for j in range(width):
                imgTestingNumbers[i, j] = 1
    imgGray = cv2.cvtColor(imgTestingNumbers, cv2.COLOR_BGR2GRAY)
    imgThresh = cv2.adaptiveThreshold(imgGray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 111, 2)
    arr.append(imgThresh)
    file_name = f"CreS2
    cv2.imwrite(file_name, arr[count - 1])
    cv2.imwrite("wordseg.png", arr[count - 1])
    cv2.imshow("shown", imgThresh)
    cv2.waitKey(0)
    return imgThresh
word_segmenter(1)
