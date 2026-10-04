
import os
import glob
from PIL import Image
def get_image_paths(folder_path):
    image_paths = glob.glob(os.path.join(folder_path, "*.jpg"))
    if not image_paths:
        raise FileNotFoundError(f"Error: Path not found or no images in {folder_path}")
    return image_paths
def rotate_and_save_images(image_paths, output_folder):
    rotations = [180, 270, 350]
    for image_path in image_paths:
        image_name = os.path.splitext(os.path.basename(image_path))[0]
        print(f"Processing image: {image_name}")
        img = Image.open(image_path)
        for idx, angle in enumerate(rotations, start=1):
            rotated_img = img.rotate(angle)
            output_path = os.path.join(output_folder, f"{image_name}_{idx}.jpg")
            rotated_img.save(output_path)
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