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
    ap.add_argument("-d", "--image_train", required=True, help="path for the images that you're going to train")
    args = vars(ap.parse_args())
    imgTrainingNumbers = cv2.imread(args["image_train"])
    if imgTrainingNumbers is None:
        print("Error: Image not read from file\n\n")
        os.system("pause")
        return
    imgGray = cv2.cvtColor(imgTrainingNumbers, cv2.COLOR_BGR2GRAY)
    imgBlurred = cv2.GaussianBlur(imgGray, (5, 5), 0)
    imgThresh = cv2.adaptiveThreshold(imgBlurred,
                                      255,
                                      cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv2.THRESH_BINARY_INV,
                                      11,
                                      2)
    cv2.imshow("imgThresh", imgThresh)
    imgThreshCopy = imgThresh.copy()
    npaContours, npaHierarchy = cv2.findContours(imgThreshCopy,
                                                 cv2.RETR_EXTERNAL,
                                                 cv2.CHAIN_APPROX_SIMPLE)
    npaFlattenedImages = np.empty((0, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT))
    intClassifications = []
    intValidChars = [ord(ch) for ch in '0123456789abcdefghijklmnopqrstuvwxyz']
    for npaContour in npaContours:
        if cv2.contourArea(npaContour) > MIN_CONTOUR_AREA:
            [intX, intY, intW, intH] = cv2.boundingRect(npaContour)
            cv2.rectangle(imgTrainingNumbers,
                          (intX, intY),
                          (intX + intW, intY + intH),
                          (0, 0, 255),
                          2)
            imgROI = imgThresh[intY:intY + intH, intX:intX + intW]
            imgROIResized = cv2.resize(imgROI, (RESIZED_IMAGE_WIDTH, RESIZED_IMAGE_HEIGHT))
            cv2.imshow("imgROI", imgROI)
            cv2.imshow("imgROIResized", imgROIResized)
            cv2.imshow("training_numbers.png", imgTrainingNumbers)
            intChar = cv2.waitKey(0)
            if intChar == 27:
                sys.exit()
            elif intChar in intValidChars:
                intClassifications.append(intChar)
                npaFlattenedImage = imgROIResized.reshape((1, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT))
                npaFlattenedImages = np.append(npaFlattenedImages, npaFlattenedImage, 0)
    fltClassifications = np.array(intClassifications, np.float32)
    npaClassifications = fltClassifications.reshape((fltClassifications.size, 1))
    print("\n\nTraining complete!\n")
    np.savetxt("classifications.txt", npaClassifications)
    np.savetxt("flattened_images.txt", npaFlattenedImages)
    changeCaption()
    cv2.destroyAllWindows()
def changeCaption():
    data = np.loadtxt("classifications.txt")
    i = 0
    for a in data:
        a = int(round(a))
        if a >= ord('a') and a <= ord('z'):
            data[i] = ord(chr(a).upper())
        i += 1
    hasil = np.array(data, np.float32)
    npaClassifications = hasil.reshape((hasil.size, 1))
    np.savetxt("classifications.txt", npaClassifications)
if __name__ == "__main__":
    main()