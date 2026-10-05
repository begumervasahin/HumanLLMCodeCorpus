import cv2
import cv2.aruco as aruco
b1 = cv2.VideoCapture(1)
'''
b1.set(cv2.CAP_PROP_AUTOFOCUS, 0)
b1.set(3, 720)
b1.set(4, 720)
'''
a1 = 0
while True:
    ret, b2 = b1.read()
    b3 = b2
    b4 = aruco.Dictionary_get(aruco.DICT_6X6_250)
    b5 = aruco.DetectorParameters_create()
    corners, ids, b6 = aruco.detectMarkers(b3, b4, b5=b5)
    b3 = aruco.drawDetectedMarkers(b3, corners, ids)
    cv2.imshow('b2', b3)
    if cv2.waitKey(1) & b7 = = ord('q'):
        break
    a1 += 1
b1.release()
cv2.destroyAllWindows()