import cv2
import os
def main():
    name = input("Enter the classifier name: ")
    path = "images/" + name
    os.makedirs(path, exist_ok=True)
    print("Folder created for:", name)
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame = cv2.flip(frame, 1)
            out.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    vidcap = cv2.VideoCapture('output.avi')
    success, image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite('images/' + name + '/frame%d.jpg' % count, image)
        print('Saved frame%d.jpg' % count)
        success, image = vidcap.read()
        count += 1
if __name__ == "__main__":
    main()