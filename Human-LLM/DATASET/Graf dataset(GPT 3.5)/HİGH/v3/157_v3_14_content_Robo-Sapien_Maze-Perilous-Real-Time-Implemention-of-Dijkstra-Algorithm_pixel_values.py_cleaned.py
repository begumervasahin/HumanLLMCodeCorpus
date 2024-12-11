import cv2
def fonk1(b5):
    b1 = cv2.imread(b5)
    height, width, b2 = b1.shape
    b3 = cv2.FONT_HERSHEY_SIMPLEX
    for i in range(0, height, 100):
        for j in range(0, width, 100):
            b4 = b1[j, i]
            cv2.putText(b1, str(b4), (i, j), b3, 0.4, (255, 255, 255), 2)
            cv2.circle(b1, (i, j), 3, (255, 255, 255), 1)
    cv2.imshow('Image', b1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
b5 = 'newa4.jpg'
fonk1(b5)