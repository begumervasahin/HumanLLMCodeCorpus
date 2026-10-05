import cv2
import cv2.aruco as aruco
cap = cv2.VideoCapture(1)
'''
cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
cap.set(3, 720)
cap.set(4, 720)
'''
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters = aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    frame_with_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)
    cv2.imshow('frame', frame_with_markers)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()