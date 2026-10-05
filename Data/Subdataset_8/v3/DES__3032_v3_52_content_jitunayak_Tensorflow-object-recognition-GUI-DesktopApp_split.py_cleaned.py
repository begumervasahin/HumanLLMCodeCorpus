import cv2
import os
def create_image_folder(classifier_name):
    folder_path = os.path.join("images", classifier_name)
    os.makedirs(folder_path, exist_ok=True)
    print("Folder created for:", classifier_name)
    return folder_path
def record_video_and_extract_frames(classifier_name):
    video_capture = cv2.VideoCapture(0)
    video_codec = cv2.VideoWriter_fourcc(*'XVID')
    video_output = cv2.VideoWriter('output.avi', video_codec, 20.0, (640, 480))
    frame_count = 0
    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if ret:
            frame = cv2.flip(frame, 1)
            video_output.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            cv2.imwrite(f'images/{classifier_name}/frame{frame_count}.jpg', frame)
            print(f'Saved frame{frame_count}.jpg')
            frame_count += 1
        else:
            break
    video_capture.release()
    video_output.release()
    cv2.destroyAllWindows()
def main():
    classifier_name = input("Enter the classifier name: ")
    image_folder_path = create_image_folder(classifier_name)
    record_video_and_extract_frames(classifier_name)
if __name__ == "__main__":
    main()