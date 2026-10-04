import cv2
import cv2.aruco as aruco
def configure_camera_settings(cap):
def detect_and_draw_markers(frame, aruco_dict, parameters):
    corners, ids, _ = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    frame_with_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)
    return frame_with_markers
def main():
    cap = cv2.VideoCapture(1)
    configure_camera_settings(cap)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters = aruco.DetectorParameters_create()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame. Exiting...")
            break
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_with_markers = detect_and_draw_markers(gray_frame, aruco_dict, parameters)
        cv2.imshow('Frame with ArUco Markers', frame_with_markers)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()