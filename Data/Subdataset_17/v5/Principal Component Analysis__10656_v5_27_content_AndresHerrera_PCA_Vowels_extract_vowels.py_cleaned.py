import os
import cv2
import numpy as np
WIDTH = 20
HEIGHT = 20
MIN_CONTOUR_AREA = 100
def process_image(image_path, output_folder):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    thresh_image = cv2.adaptiveThreshold(blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    cv2.imshow("Threshold Image", thresh_image)
    contours, _ = cv2.findContours(thresh_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    vowel_count = 0
    for contour in contours:
        if cv2.contourArea(contour) > MIN_CONTOUR_AREA:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            roi = thresh_image[y:y + h, x:x + w]
            resized_roi = cv2.resize(roi, (WIDTH, HEIGHT))
            cv2.imshow("Processed Image", image)
            vowel_count += 1
            cv2.imwrite(f'{output_folder}/vowel_{vowel_count}.png', cv2.bitwise_not(resized_roi))
    return vowel_count
def main():
    image_path = "raw_vowels.jpg"
    output_folder = "vowels"
    os.makedirs(output_folder, exist_ok=True)
    vowel_count = process_image(image_path, output_folder)
    print(f"{vowel_count} files written into '{output_folder}' folder!")
    print("Notice: You have to arrange the files into the 'training' folder tree:")
    print(" - training/A  <-  store only A images")
    print(" - training/E  <-  store only E images")
    print(" - training/I  <-  store only I images")
    print(" - training/O  <-  store only O images")
    print(" - training/U  <-  store only U images")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()