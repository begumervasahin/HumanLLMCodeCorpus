import cv2
import numpy as np
def fonk1(image_path, b1 = 100):
    b2 = cv2.imread(image_path)
    height, width, b3 = b2.shape
    print(f"Image dimensions: {height}x{width}x{b3}")
    b4 = cv2.FONT_HERSHEY_SIMPLEX
    for y in range(0, height, b1):
        for x in range(0, width, b1):
            b5 = b2[y, x]
            b6 = str(tuple(b5))
            cv2.putText(b2, b6, (x, y), b4, 0.4, (255, 255, 255), 1)
            cv2.circle(b2, (x, y), 3, (255, 255, 255), 1)
    cv2.imshow('Annotated Image', b2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if b7 = = "__main__":
    fonk1('newa4.jpg')