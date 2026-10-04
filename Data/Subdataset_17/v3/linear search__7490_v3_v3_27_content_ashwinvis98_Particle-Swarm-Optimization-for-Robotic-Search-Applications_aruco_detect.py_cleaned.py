import cv2
import cv2.aruco as aruco
def main():
    video_capture = cv2.VideoCapture(1)
    '''
    video_capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    '''
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        processed_frame = process_frame(frame)
        show_frame(processed_frame)
        if check_key_press('q'):
            break
    cleanup(video_capture)
def process_frame(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, _ = detect_aruco_markers(gray_frame)
    return draw_markers(frame.copy(), corners, ids)
def detect_aruco_markers(gray_frame):
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters = aruco.DetectorParameters_create()
    corners, ids, rejected_points = aruco.detectMarkers(gray_frame, aruco_dict, parameters=parameters)
    return corners, ids, rejected_points
def draw_markers(frame, corners, ids):
    return aruco.drawDetectedMarkers(frame, corners, ids)
def show_frame(frame):
    cv2.imshow('Frame with ArUco Markers', frame)
def check_key_press(key):
    return cv2.waitKey(1) & 0xFF == ord(key)
def cleanup(video_capture):
    video_capture.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()