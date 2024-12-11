import cv2
import cv2.aruco as aruco
def fonk1():
    b1 = cv2.VideoCapture(1)
    '''
    b1.set(cv2.CAP_PROP_AUTOFOCUS, 0)
    b1.set(3, 720)
    b1.set(4, 720)
    '''
    while True:
        ret, b2 = b1.read()
        b3 = cv2.cvtColor(b2, cv2.COLOR_BGR2GRAY)
        corners, ids, b4 = fonk2(b3)
        b5 = fonk3(b2.copy(), corners, ids)
        fonk4(b5)
        if fonk5():
            break
    fonk6(b1)
    fonk7()
def fonk2(b2):
    b6 = aruco.Dictionary_get(aruco.DICT_6X6_250)
    b7 = aruco.DetectorParameters_create()
    corners, ids, b4 = aruco.detectMarkers(b2, b6, parameters=b7)
    return corners, ids, b4
def fonk3(b2, corners, ids):
    b5 = aruco.drawDetectedMarkers(b2, corners, ids)
    return b5
def fonk4(b2):
    cv2.imshow('Frame with ArUco Markers', b2)
def fonk5():
    return cv2.waitKey(1) & b8 = = ord('q')
def fonk6(b1):
    b1.release()
def fonk7():
    cv2.destroyAllWindows()
if b9 = = "__main__":
    fonk1()