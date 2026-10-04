import cv2
import cv2.aruco as aruco
def fonk1():
    b1 = fonk2()
    while True:
        ret, b2 = fonk3(b1)
        if not ret:
            print("Failed to capture image")
            break
        b3 = fonk4(b2)
        corners, ids, b4 = fonk5(b3)
        b5 = fonk6(b2, corners, ids)
        fonk7(b5)
        if fonk8('q'):
            break
    fonk9(b1)
def fonk2():
    b1 = cv2.VideoCapture(1)
    return b1
def fonk3(b1):
    return b1.read()
def fonk4(b2):
    return cv2.cvtColor(b2, cv2.COLOR_BGR2GRAY)
def fonk5(b2):
    b6 = aruco.Dictionary_get(aruco.DICT_6X6_250)
    b7 = aruco.DetectorParameters_create()
    corners, ids, b4 = aruco.detectMarkers(b2, b6, parameters=b7)
    return corners, ids, b4
def fonk6(b2, corners, ids):
    return aruco.drawDetectedMarkers(b2, corners, ids)
def fonk7(b2):
    cv2.imshow('Frame with ArUco Markers', b2)
def fonk8(key):
    return cv2.waitKey(1) & b8 = = ord(key)
def fonk9(b1):
    b1.release()
    cv2.destroyAllWindows()
if b9 = = "__main__":
    fonk1()