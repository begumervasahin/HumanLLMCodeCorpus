import cv2
import os
INPUT_DIRECTORY = "images/"
OUTPUT_DIRECTORY = "faces/"
def facecrop(image_path):
    facedata = "haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(facedata)
    img = cv2.imread(image_path)
    if img is None:
        print(f"Could not read image: {image_path}")
        return
    try:
        faces = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in faces:
            sub_face = img[y:y + h, x:x + w]
            file_name = os.path.basename(image_path)
            output_path = os.path.join(OUTPUT_DIRECTORY, file_name)
            cv2.imwrite(output_path, sub_face)
            print(f"Writing: {output_path}")
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
def main():
    ensure_directory_exists(OUTPUT_DIRECTORY)
    images = os.listdir(INPUT_DIRECTORY)
    for index, image_file in enumerate(images):
        image_path = os.path.join(INPUT_DIRECTORY, image_file)
        print(f"Processing {index + 1}/{len(images)}: {image_file}")
        facecrop(image_path)
if __name__ == '__main__':
    main()