import cv2
import os
input_directory = "images/"
output_directory = "faces/"
def detect_and_crop_faces(image_path):
    face_cascade = "haarcascade_frontalface_alt.xml"
    face_detector = cv2.CascadeClassifier(face_cascade)
    image = cv2.imread(image_path)
    if image is None:
        print(f"Could not read image: {image_path}")
        return
    try:
        minisize = (image.shape[1], image.shape[0])
        miniframe = cv2.resize(image, minisize)
        faces = face_detector.detectMultiScale(miniframe)
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cropped_face = image[y:y + h, x:x + w]
            file_name = os.path.basename(image_path)
            output_path = os.path.join(output_directory, file_name)
            cv2.imwrite(output_path, cropped_face)
            print(f"Saved cropped face to: {output_path}")
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
if __name__ == '__main__':
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    image_files = os.listdir(input_directory)
    for index, image_file in enumerate(image_files):
        image_path = os.path.join(input_directory, image_file)
        print(f"Processing {index + 1}/{len(image_files)}: {image_file}")
        detect_and_crop_faces(image_path)