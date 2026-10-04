import os
import cv2
import numpy as np
WIDTH, HEIGHT = 20, 20
MIN_CONTOUR_AREA = 100
def load_and_preprocess_image(image_path):
    imgVowels = cv2.imread(image_path)
    if imgVowels is None:
        raise FileNotFoundError(f"Error: Image '{image_path}' not found or unable to read image.")
    imgGray = cv2.cvtColor(imgVowels, cv2.COLOR_BGR2GRAY)
    imgBlurred = cv2.GaussianBlur(imgGray, (5, 5), 0)
    imgThresh = cv2.adaptiveThreshold(
        imgBlurred,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        11,
        2
    )
    return imgThresh, imgVowels
def find_and_process_contours(imgThresh, imgVowels):
    imgThreshCopy = imgThresh.copy()
    contours, _ = cv2.findContours(
        imgThreshCopy,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )
    found = 0
    for contour in contours:
        if cv2.contourArea(contour) > MIN_CONTOUR_AREA:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(imgVowels, (x, y), (x + w, y + h), (0, 0, 255), 2)
            imgROI = imgThresh[y:y + h, x:x + w]
            imgROIResized = cv2.resize(imgROI, (WIDTH, HEIGHT))
            cv2.imshow("Original File", imgVowels)
            found += 1
            os.makedirs('vowels', exist_ok=True)
            cv2.imwrite(f'vowels/vowel_{found}.png', cv2.bitwise_not(imgROIResized))
    return found
def main():
    image_path = "raw_vowels.jpg"
    try:
        imgThresh, imgVowels = load_and_preprocess_image(image_path)
        cv2.imshow("Threshold Image", imgThresh)
        found_files = find_and_process_contours(imgThresh, imgVowels)
        print(f"{found_files} files written into (vowels) folder!")
        print("Notice: You have to arrange (vowels) files into (training) folder tree!")
        print("in folder :  training/A  <-  store only A images")
        print("in folder :  training/E  <-  store only E images")
        print("in folder :  training/I  <-  store only I images")
        print("in folder :  training/O  <-  store only O images")
        print("in folder :  training/U  <-  store only U images")
        cv2.waitKey(0)
    except FileNotFoundError as e:
        print(e)
    finally:
        cv2.destroyAllWindows()
if __name__ == "__main__":
    main()