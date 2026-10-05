import argparse
import os
import sys
import cv2
import numpy as np
MIN_CONTOUR_AREA = 100
RESIZED_IMAGE_WIDTH = 20
RESIZED_IMAGE_HEIGHT = 30
def main():
    args = parse_arguments()
    if args.image_train:
        img_training = read_image(args.image_train)
        if img_training is None:
            print("Error: Failed to read the image from file")
            return
    else:
        print("Please provide the path to the training image using the '-d' or '--image_train' argument.")
        return
    img_thresh = preprocess_image(img_training)
    process_contours(img_thresh)
    save_classification_data()
    change_lowercase_to_uppercase()
    cv2.destroyAllWindows()
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--image_train", help="Path to the training image")
    return parser.parse_args()
def read_image(image_path):
    img = cv2.imread(image_path)
    return img
def preprocess_image(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blurred = cv2.GaussianBlur(img_gray, (5, 5), 0)
    img_thresh = cv2.adaptiveThreshold(img_blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv2.THRESH_BINARY_INV, 11, 2)
    cv2.imshow("imgThresh", img_thresh)
    return img_thresh
def process_contours(img_thresh):
    _, contours, _ = cv2.findContours(img_thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    flattened_images = np.empty((0, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT))
    classifications = []
    for contour in contours:
        if cv2.contourArea(contour) > MIN_CONTOUR_AREA:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(img_training, (x, y), (x + w, y + h), (0, 0, 255), 2)
            roi = img_thresh[y:y + h, x:x + w]
            roi_resized = cv2.resize(roi, (RESIZED_IMAGE_WIDTH, RESIZED_IMAGE_HEIGHT))
            cv2.imshow("imgROI", roi)
            cv2.imshow("imgROIResized", roi_resized)
            cv2.imshow("training_numbers.png", img_training)
            char_code = cv2.waitKey(0)
            if char_code == 27:
                sys.exit()
            elif 48 <= char_code <= 122:
                classifications.append(char_code)
                flattened_image = roi_resized.reshape((1, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT))
                flattened_images = np.append(flattened_images, flattened_image, 0)
    return classifications, flattened_images
def save_classification_data():
    np.savetxt("classifications.txt", classifications)
    np.savetxt("flattened_images.txt", flattened_images)
    print("\nTraining complete!!\n")
def change_lowercase_to_uppercase():
    data = np.loadtxt("classifications.txt")
    data = np.where((data >= 97) & (data <= 122), data - 32, data)
    np.savetxt("classifications.txt", data)
if __name__ == "__main__":
    main()