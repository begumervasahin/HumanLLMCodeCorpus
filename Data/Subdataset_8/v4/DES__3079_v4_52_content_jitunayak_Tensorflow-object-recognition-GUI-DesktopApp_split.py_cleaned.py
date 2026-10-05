import cv2
import os
def main():
    classifier_name = input("Enter the classifier name: ")
    image_folder_path = "images/" + classifier_name
    os.makedirs(image_folder_path, exist_ok=True)
    print("Folder created for:", classifier_name)
    video_capture = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output_video = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if ret:
            frame = cv2.flip(frame, 1)
            output_video.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    video_capture.release()
    output_video.release()
    cv2.destroyAllWindows()
    video_reader = cv2.VideoCapture('output.avi')
    success, image = video_reader.read()
    count = 0
    while success:
        cv2.imwrite(f'images/{classifier_name}/frame{count}.jpg', image)
        print('Saved frame%d.jpg' % count)
        success, image = video_reader.read()
        count += 1
if __name__ == "__main__":
    main()