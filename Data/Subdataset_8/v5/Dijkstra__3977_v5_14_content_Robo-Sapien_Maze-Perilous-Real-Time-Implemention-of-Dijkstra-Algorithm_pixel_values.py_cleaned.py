import cv2
import numpy as np
def display_color_info(image):
    FONT = cv2.FONT_HERSHEY_SIMPLEX
    STEP_SIZE = 100
    height, width, _ = image.shape
    print("Image shape:", image.shape)
    for i in range(0, height, STEP_SIZE):
        for j in range(0, width, STEP_SIZE):
            color = image[j, i]
            cv2.putText(image, str(color), (i, j), FONT, 0.4, (255, 255, 255), 2)
            cv2.circle(image, (i, j), 3, (255, 255, 255), 1)
    cv2.imshow('img', image)
    cv2.waitKey(0) & 0xFF
    cv2.destroyAllWindows()
if __name__ == "__main__":
    img = cv2.imread('newa4.jpg')
    display_color_info(img)