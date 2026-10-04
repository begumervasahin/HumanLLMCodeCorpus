import os
import array
import numpy as np
import cv2
segmented_images = []
def word_segmenter(count):
    img_path = "words.png"
    img = cv2.imread(img_path)
    if img is None:
        print("Error: image not read from file")
        os.system("pause")
        return
    height, width, channels = img.shape
    print(f"Height: {height}")
    print(f"Width: {width}")
    word_ratio = float(width) / float(height)
    print(f"Ratio: {word_ratio}")
    if word_ratio >= 0.9:
        max_val = 9999
        min_val = -999
        count_array = array.array('i', (0,) * 100)
        inew = -1
        inew0 = -1
        for i in range(0, height
            for j in range(width):
                if np.any(img[i, j] == 0):
                    count_array[i] += 1
            if count_array[i] < max_val:
                max_val = count_array[i]
                inew = i
            elif count_array[i] - max_val <= width
                inew0 = i
        irange = max(inew, inew0)
        for i in range(inew - 2, irange + 2):
            for j in range(width):
                img[i, j] = 1
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_thresh = cv2.adaptiveThreshold(
        img_gray,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY_INV,
        111,
        2
    )
    segmented_images.append(img_thresh)
    save_segmented_image(count, segmented_images[count - 1])
    cv2.imwrite("wordseg.png", segmented_images[count])
    cv2.imshow("Segmented Image", img_thresh)
    cv2.waitKey(0)
    return img_thresh
def save_segmented_image(count, image):
    save_path = f"CreS2/c{count - 1}.png" if count > 0 else "CreS2/c-1.png"
    cv2.imwrite(save_path, image)
if __name__ == "__main__":
    count = int(input("Enter count: "))
    word_segmenter(count)