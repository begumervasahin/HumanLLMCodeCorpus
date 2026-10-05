import cv2
def display_grid_cells_with_color_info(image_path):
    img = cv2.imread(image_path)
    height, width, _ = img.shape
    font = cv2.FONT_HERSHEY_SIMPLEX
    for i in range(0, height, 100):
        for j in range(0, width, 100):
            color = img[j, i]
            cv2.putText(img, str(color), (i, j), font, 0.4, (255, 255, 255), 2)
            cv2.circle(img, (i, j), 3, (255, 255, 255), 1)
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
image_path = 'newa4.jpg'
display_grid_cells_with_color_info(image_path)