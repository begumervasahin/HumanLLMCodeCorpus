import cv2
import cv2.aruco as aruco
video_capture = cv2.VideoCapture(1)
'''
video_capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)
video_capture.set(3, 720)
video_capture.set(4, 720)
'''
while True:
    ret, frame = video_capture.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dictionary = aruco.Dictionary_get(aruco.DICT_6X6_250)
    detection_parameters = aruco.DetectorParameters_create()
    corners, ids, rejected_image_points = aruco.detectMarkers(gray_frame, aruco_dictionary, parameters=detection_parameters)
    frame_with_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)
    cv2.imshow('Frame with ArUco Markers', frame_with_markers)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()