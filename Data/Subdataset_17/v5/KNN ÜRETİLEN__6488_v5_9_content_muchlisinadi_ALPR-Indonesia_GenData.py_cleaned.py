import argparse
import os
import sys
import cv2
import numpy as np
MIN_CONTOUR_AREA = 100
RESIZED_IMAGE_WIDTH = 20
RESIZED_IMAGE_HEIGHT = 30
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--image_train", required=True, help="Path for the images that you're going to train")
    args = ap.parse_args()
    img_training_numbers = cv2.imread(args.image_train)
    if img_training_numbers is None:
        print("Error: Image not read from file\n")
        sys.exit()
    img_thresh = preprocess_image(img_training_numbers)
    cv2.imshow("Threshold Image", img_thresh)
    flattened_images, classifications = extract_and_classify_contours(img_thresh, img_training_numbers)
    print("\nTraining complete!\n")
    np.savetxt("classifications.txt", classifications)
    np.savetxt("flattened_images.txt", flattened_images)
    update_classifications()
    cv2.destroyAllWindows()
def preprocess_image(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blurred = cv2.GaussianBlur(img_gray, (5, 5), 0)
    img_thresh = cv2.adaptiveThreshold(
        img_blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    return img_thresh
def extract_and_classify_contours(img_thresh, img_training_numbers):
    img_thresh_copy = img_thresh.copy()
    contours, hierarchy = cv2.findContours(
        img_thresh_copy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    flattened_images = np.empty((0, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT))
    classifications = []
    valid_chars = [ord(char) for char in '0123456789abcdefghijklmnopqrstuvwxyz']
    for contour in contours:
        if cv2.contourArea(contour) > MIN_CONTOUR_AREA:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(img_training_numbers, (x, y), (x + w, y + h), (0, 0, 255), 2)
            img_roi = img_thresh[y:y + h, x:x + w]
            img_roi_resized = cv2.resize(img_roi, (RESIZED_IMAGE_WIDTH, RESIZED_IMAGE_HEIGHT))
            cv2.imshow("ROI", img_roi)
            cv2.imshow("Resized ROI", img_roi_resized)
            cv2.imshow("Training Numbers", img_training_numbers)
            int_char = cv2.waitKey(0)
            if int_char == 27:
                sys.exit()
            elif int_char in valid_chars:
                classifications.append(int_char)
                flattened_image = img_roi_resized.reshape((1, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT))
                flattened_images = np.append(flattened_images, flattened_image, axis=0)
    classifications = np.array(classifications, np.float32).reshape((-1, 1))
    return flattened_images, classifications
def update_classifications():
    data = np.loadtxt("classifications.txt", dtype=np.float32)
    updated_data = [(val - 32 if ord('a') <= val <= ord('z') else val) for val in data]
    updated_classifications = np.array(updated_data, np.float32).reshape((-1, 1))
    np.savetxt("classifications.txt", updated_classifications)
if __name__ == "__main__":
    main()