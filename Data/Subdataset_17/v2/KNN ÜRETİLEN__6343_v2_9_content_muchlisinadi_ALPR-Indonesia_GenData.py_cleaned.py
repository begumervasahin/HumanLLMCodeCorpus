import argparse
import os
import sys
import cv2
import numpy as np
MIN_CONTOUR_AREA = 100
RESIZED_IMAGE_WIDTH = 20
RESIZED_IMAGE_HEIGHT = 30
def main():
    parser = argparse.ArgumentParser(description="Train an OCR model on provided image data.")
    parser.add_argument("-d", "--image_train", required=True, help="Path to the training image.")
    args = parser.parse_args()
    img_training_numbers = cv2.imread(args.image_train)
    if img_training_numbers is None:
        print("Error: Image not read from file")
        sys.exit(1)
    img_gray = cv2.cvtColor(img_training_numbers, cv2.COLOR_BGR2GRAY)
    img_blurred = cv2.GaussianBlur(img_gray, (5, 5), 0)
    img_thresh = cv2.adaptiveThreshold(img_blurred,
                                       255,
                                       cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv2.THRESH_BINARY_INV,
                                       11,
                                       2)
    cv2.imshow("Threshold Image", img_thresh)
    img_thresh_copy = img_thresh.copy()
    contours, _ = cv2.findContours(img_thresh_copy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    flattened_images = np.empty((0, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT))
    classifications = []
    valid_chars = [ord(ch) for ch in '0123456789abcdefghijklmnopqrstuvwxyz']
    for contour in contours:
        if cv2.contourArea(contour) > MIN_CONTOUR_AREA:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(img_training_numbers, (x, y), (x + w, y + h), (0, 0, 255), 2)
            img_roi = img_thresh[y:y + h, x:x + w]
            img_roi_resized = cv2.resize(img_roi, (RESIZED_IMAGE_WIDTH, RESIZED_IMAGE_HEIGHT))
            cv2.imshow("Region of Interest", img_roi)
            cv2.imshow("Resized ROI", img_roi_resized)
            cv2.imshow("Training Numbers", img_training_numbers)
            key = cv2.waitKey(0)
            if key == 27:
                sys.exit()
            elif key in valid_chars:
                classifications.append(key)
                flattened_image = img_roi_resized.reshape((1, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT))
                flattened_images = np.append(flattened_images, flattened_image, 0)
    classifications = np.array(classifications, np.float32).reshape((-1, 1))
    print("Training complete!")
    np.savetxt("classifications.txt", classifications)
    np.savetxt("flattened_images.txt", flattened_images)
    update_classifications_to_uppercase()
    cv2.destroyAllWindows()
def update_classifications_to_uppercase():
    classifications = np.loadtxt("classifications.txt")
    classifications = np.array([ord(chr(int(round(c))).upper()) if 'a' <= chr(int(round(c))) <= 'z' else c for c in classifications], np.float32)
    classifications = classifications.reshape((-1, 1))
    np.savetxt("classifications.txt", classifications)
if __name__ == "__main__":
    main()