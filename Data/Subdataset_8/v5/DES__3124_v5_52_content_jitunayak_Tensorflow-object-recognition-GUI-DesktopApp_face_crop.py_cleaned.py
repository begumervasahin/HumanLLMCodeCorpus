import cv2
import os
input_directory = "/images"
output_directory = "/images/cropped/"
def detect_and_crop_faces(image_path):
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    img = cv2.imread(image_path)
    try:
        minisize = (img.shape[1], img.shape[0])
        miniframe = cv2.resize(img, minisize)
        faces = face_cascade.detectMultiScale(miniframe)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            sub_face = img[y:y + h, x:x + w]
            filename = os.path.basename(image_path)
            cv2.imwrite(os.path.join(output_directory, filename), sub_face)
            print("Saved cropped face:", filename)
    except Exception as e:
        print("Error:", e)
if __name__ == '__main__':
    images = os.listdir(input_directory)
    for i, img in enumerate(images, 1):
        image_path = os.path.join(input_directory, img)
        print(f"Processing image {i}/{len(images)}: {image_path}")
        detect_and_crop_faces(image_path)