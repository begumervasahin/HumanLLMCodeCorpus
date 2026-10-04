
import os
import glob
import numpy as np
import cv2
from PIL import Image
def get_image_paths(folder_path):
    image_paths = glob.glob(os.path.join(folder_path, "*.jpg"))
    if not image_paths:
        raise FileNotFoundError("Error: Path not found to train data folder.")
    return image_paths
def rotate_and_save_images(image_paths, output_folder):
    for image_path in image_paths:
        imagename = os.path.splitext(os.path.basename(image_path))[0]
        print(f"Processing image: {imagename}")
        temp = cv2.imread(image_path)
        img = Image.fromarray(temp)
        rotations = [180, 270, 350]
        for idx, angle in enumerate(rotations, start=1):
            rotated_img = img.rotate(angle)
            output_path = os.path.join(output_folder, f"{imagename}_{idx}.jpg")
            cv2.imwrite(output_path, np.array(rotated_img))
            print(f"Saved rotated image: {output_path}")
def main():
    train_data_folder = os.path.join("Data", "train", "destructed")
    try:
        train_destructed_paths = get_image_paths(train_data_folder)
        print("Successfully read train data folder path!")
        print("Total images:", len(train_destructed_paths))
        rotate_and_save_images(train_destructed_paths, train_data_folder)
    except FileNotFoundError as e:
        print(e)
if __name__ == "__main__":
    main()