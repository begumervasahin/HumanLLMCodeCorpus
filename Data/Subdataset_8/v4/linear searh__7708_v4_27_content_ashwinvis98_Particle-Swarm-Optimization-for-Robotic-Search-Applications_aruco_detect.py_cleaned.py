import cv2
import cv2.aruco as aruco
cap = cv2.VideoCapture(1)
'''
cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
cap.set(3, 720)
cap.set(4, 720)
'''
frame_counter = 0
while True:
    ret, frame = cap.read()
    gray = frame
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters = aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    gray = aruco.drawDetectedMarkers(gray, corners, ids)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    frame_counter += 1
cap.release()
cv2.destroyAllWindows()