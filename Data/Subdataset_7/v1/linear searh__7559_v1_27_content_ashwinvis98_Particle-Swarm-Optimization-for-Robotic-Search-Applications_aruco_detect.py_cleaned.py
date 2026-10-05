import cv2
import cv2.aruco as aruco
b1 = cv2.VideoCapture(1)
'''
b1.set(cv2.CAP_PROP_AUTOFOCUS, 0)
b1.set(3, 720)
b1.set(4, 720)
'''
while True:
    ret, b2 = b1.read()
    b3 = cv2.cvtColor(b2, cv2.COLOR_BGR2GRAY)
    b4 = aruco.Dictionary_get(aruco.DICT_6X6_250)
    b5 = aruco.DetectorParameters_create()
    corners, ids, b6 = aruco.detectMarkers(b3, b4, b5=b5)
    b7 = aruco.drawDetectedMarkers(b2.copy(), corners, ids)
    cv2.imshow('b2', b7)
    if cv2.waitKey(1) & b8 = = ord('q'):
        break
b1.release()
cv2.destroyAllWindows()