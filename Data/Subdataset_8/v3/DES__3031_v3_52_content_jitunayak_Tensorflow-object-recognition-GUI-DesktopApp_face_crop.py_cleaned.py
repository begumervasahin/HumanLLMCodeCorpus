import cv2
import os
input_directory = "images"
output_directory = "cropped_images/"
def detect_and_crop_faces(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
    img = cv2.imread(image_path)
    minisize = (img.shape[1], img.shape[0])
    miniframe = cv2.resize(img, minisize)
    faces = face_cascade.detectMultiScale(miniframe)
    for (x, y, w, h) in faces:
        face_img = img[y:y+h, x:x+w]
        face_filename = os.path.basename(image_path)
        output_path = os.path.join(output_directory, face_filename)
        cv2.imwrite(output_path, face_img)
        print(f"Detected and saved face: {output_path}")
if __name__ == '__main__':
    image_files = os.listdir(input_directory)
    for i, image_file in enumerate(image_files, start=1):
        image_path = os.path.join(input_directory, image_file)
        print(f"Processing image {i}/{len(image_files)}: {image_file}")
        detect_and_crop_faces(image_path)