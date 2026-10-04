import cv2
import cv2.aruco as aruco
def main():
    video_capture = cv2.VideoCapture(1)
    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to capture image")
            break
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners, ids, rejected_image_points = detect_aruco_markers(gray_frame)
        frame_with_markers = draw_markers(frame, corners, ids)
        show_frame(frame_with_markers)
        if check_key_press():
            break
    release_video_capture(video_capture)
    close_windows()
def detect_aruco_markers(frame):
    aruco_dictionary = aruco.Dictionary_get(aruco.DICT_6X6_250)
    detection_parameters = aruco.DetectorParameters_create()
    corners, ids, rejected_image_points = aruco.detectMarkers(frame, aruco_dictionary, parameters=detection_parameters)
    return corners, ids, rejected_image_points
def draw_markers(frame, corners, ids):
    frame_with_markers = aruco.drawDetectedMarkers(frame, corners, ids)
    return frame_with_markers
def show_frame(frame):
    cv2.imshow('Frame with ArUco Markers', frame)
def check_key_press():
    return cv2.waitKey(1) & 0xFF == ord('q')
def release_video_capture(video_capture):
    video_capture.release()
def close_windows():
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()