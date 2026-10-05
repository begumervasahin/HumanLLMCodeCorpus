import PIL
import glob
import os.path
import numpy as np
import cv2
def main():
    train_data_folder = os.path.join("Data", "train", "destructed", "*.jpg")
    train_destructed_paths = glob.glob(train_data_folder)
    if not train_destructed_paths:
        print("Error: Path not found to train data folder..")
        return
    print("Successfully read train data folder path..!")
    print("Total images:", len(train_destructed_paths))
    for img_path in train_destructed_paths:
        process_image(img_path)
def process_image(img_path):
    img_name = os.path.splitext(os.path.basename(img_path))[0]
    print(img_name)
    img = cv2.imread(img_path)
    pil_img = PIL.Image.fromarray(img)
    write_path = os.path.join("Data", "train", "destructed")
    for angle in [180, 270, 350]:
        rotated_img = pil_img.rotate(angle)
        cv2.imwrite(os.path.join(write_path, f"{img_name}_{angle}.jpg"), np.array(rotated_img))
if __name__ == "__main__":
    main()