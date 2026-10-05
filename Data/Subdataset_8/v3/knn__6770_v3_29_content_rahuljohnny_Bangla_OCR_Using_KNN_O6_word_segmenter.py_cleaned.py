import cv2
import numpy as np
def word_segmenter(count):
    arr = []
    img_testing_numbers = cv2.imread("words.png")
    if img_testing_numbers is None:
        print("Error: image not read from file")
        return
    height, width, _ = img_testing_numbers.shape
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
                if np.any(img_testing_numbers[i, j] == 0):
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
                img_testing_numbers[i, j] = 1
    img_gray = cv2.cvtColor(img_testing_numbers, cv2.COLOR_BGR2GRAY)
    img_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 111, 2)
    arr.append(img_thresh)
    file_name = f"CreS2
    cv2.imwrite(file_name, arr[count - 1])
    cv2.imwrite("wordseg.png", arr[count - 1])
    cv2.imshow("shown", img_thresh)
    cv2.waitKey(0)
    return img_thresh
word_segmenter(1)
