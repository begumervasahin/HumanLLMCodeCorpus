import cv2
import os
def main():
    classifier_name = input("Enter the classifier name: ")
    image_folder_path = "images/" + classifier_name
    os.makedirs(image_folder_path, exist_ok=True)
    print("Folder created for:", classifier_name)
    video_capture = cv2.VideoCapture(0)
    video_codec = cv2.VideoWriter_fourcc(*'XVID')
    video_output = cv2.VideoWriter('output.avi', video_codec, 20.0, (640, 480))
    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if ret:
            frame = cv2.flip(frame, 1)
            video_output.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    video_capture.release()
    video_output.release()
    cv2.destroyAllWindows()
    video_reader = cv2.VideoCapture('output.avi')
    success, image = video_reader.read()
    frame_count = 0
    while success:
        cv2.imwrite(f'images/{classifier_name}/frame{frame_count}.jpg', image)
        print(f'Saved frame{frame_count}.jpg')
        success, image = video_reader.read()
        frame_count += 1
if __name__ == "__main__":
    main()