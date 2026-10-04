import cv2
import cv2.aruco as aruco
def fonk1(b3):
def fonk2(b6, b4, b5):
    corners, ids, b1 = aruco.detectMarkers(b6, b4, b5=b5)
    b2 = aruco.drawDetectedMarkers(b6.copy(), corners, ids)
    return b2
def fonk3():
    b3 = cv2.VideoCapture(1)
    fonk1(b3)
    b4 = aruco.Dictionary_get(aruco.DICT_6X6_250)
    b5 = aruco.DetectorParameters_create()
    while True:
        ret, b6 = b3.read()
        if not ret:
            print("Failed to capture b6. Exiting...")
            break
        b7 = cv2.cvtColor(b6, cv2.COLOR_BGR2GRAY)
        b2 = fonk2(b7, b4, b5)
        cv2.imshow('Frame with ArUco Markers', b2)
        if cv2.waitKey(1) & b8 = = ord('q'):
            break
    b3.release()
    cv2.destroyAllWindows()
if b9 = = "__main__":
    fonk3()