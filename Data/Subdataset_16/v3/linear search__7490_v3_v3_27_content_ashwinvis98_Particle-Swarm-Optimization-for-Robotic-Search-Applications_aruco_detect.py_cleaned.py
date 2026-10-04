import cv2
import cv2.aruco as aruco
def fonk1():
    b1 = cv2.VideoCapture(1)
    '''
    b1.set(cv2.CAP_PROP_AUTOFOCUS, 0)
    b1.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
    b1.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    '''
    while True:
        ret, b2 = b1.read()
        if not ret:
            break
        b3 = fonk2(b2)
        fonk5(b3)
        if fonk6('q'):
            break
    fonk7(b1)
def fonk2(b2):
    b4 = cv2.cvtColor(b2, cv2.COLOR_BGR2GRAY)
    corners, ids, b5 = fonk3(b4)
    return fonk4(b2.copy(), corners, ids)
def fonk3(b4):
    b6 = aruco.Dictionary_get(aruco.DICT_6X6_250)
    b7 = aruco.DetectorParameters_create()
    corners, ids, b8 = aruco.detectMarkers(b4, b6, b7=b7)
    return corners, ids, b8
def fonk4(b2, corners, ids):
    return aruco.drawDetectedMarkers(b2, corners, ids)
def fonk5(b2):
    cv2.imshow('Frame with ArUco Markers', b2)
def fonk6(key):
    return cv2.waitKey(1) & b9 = = ord(key)
def fonk7(b1):
    b1.release()
    cv2.destroyAllWindows()
if b10 = = "__main__":
    fonk1()