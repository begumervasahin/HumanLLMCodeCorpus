import cv2
import os
input_directory = "/images"
output_directory = "/images/cropped/"
def facecrop(image_path):
    facedata = "haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(facedata)
    img = cv2.imread(image_path)
    try:
        minisize = (img.shape[1], img.shape[0])
        miniframe = cv2.resize(img, minisize)
        faces = cascade.detectMultiScale(miniframe)
        for f in faces:
            x, y, w, h = f
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            sub_face = img[y:y + h, x:x + w]
            filename = os.path.basename(image_path)
            cv2.imwrite(output_directory + filename, sub_face)
            print("Writing: " + filename)
    except Exception as e:
        print("Error:", e)
if __name__ == '__main__':
    images = os.listdir(input_directory)
    for i, img in enumerate(images, 1):
        image_path = os.path.join(input_directory, img)
        print(i)
        facecrop(image_path)