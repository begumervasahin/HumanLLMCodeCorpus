import cv2
import os
INPUT_DIR = "images/"
OUTPUT_DIR = "faces/"
def detect_and_crop_faces(image_path):
    face_cascade_path = "haarcascade_frontalface_alt.xml"
    face_detector = cv2.CascadeClassifier(face_cascade_path)
    image = cv2.imread(image_path)
    if image is None:
        print(f"Could not read image: {image_path}")
        return
    try:
        faces = face_detector.detectMultiScale(image)
        for (x, y, w, h) in faces:
            cropped_face = image[y:y + h, x:x + w]
            file_name = os.path.basename(image_path)
            output_path = os.path.join(OUTPUT_DIR, file_name)
            cv2.imwrite(output_path, cropped_face)
            print(f"Saved cropped face to: {output_path}")
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
def main():
    ensure_directory_exists(OUTPUT_DIR)
    image_files = os.listdir(INPUT_DIR)
    for index, image_file in enumerate(image_files):
        image_path = os.path.join(INPUT_DIR, image_file)
        print(f"Processing {index + 1}/{len(image_files)}: {image_file}")
        detect_and_crop_faces(image_path)
if __name__ == '__main__':
    main()