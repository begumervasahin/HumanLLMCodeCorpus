import cv2
import numpy as np
def annotate_image_with_colors(image_path, step=100):
    img = cv2.imread(image_path)
    height, width, channels = img.shape
    print(f"Image dimensions: {height}x{width}x{channels}")
    font = cv2.FONT_HERSHEY_SIMPLEX
    for y in range(0, height, step):
        for x in range(0, width, step):
            color = img[y, x]
            color_str = str(tuple(color))
            cv2.putText(img, color_str, (x, y), font, 0.4, (255, 255, 255), 1)
            cv2.circle(img, (x, y), 3, (255, 255, 255), 1)
    cv2.imshow('Annotated Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    annotate_image_with_colors('newa4.jpg')