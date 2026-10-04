import os
from PIL import Image
import piexif
import random
def load_exif_data(image_path):
    try:
        return piexif.load(image_path)
    except (FileNotFoundError, piexif.InvalidImageDataError) as e:
        print(f"Error loading EXIF data from {image_path}: {e}")
        return None
def adjust_gps_coordinate(coordinate, offset):
    if coordinate:
        return (
            (coordinate[0][0], coordinate[0][1]),
            (coordinate[1][0], coordinate[1][1]),
            (coordinate[2][0] + offset, coordinate[2][1])
        )
    return coordinate
def update_image_gps_data(file_name, original_gps_data):
    try:
        with Image.open(file_name) as img:
            exif_dict = piexif.load(img.info.get("exif", b""))
    except (FileNotFoundError, piexif.InvalidImageDataError) as e:
        print(f"Error loading EXIF data from {file_name}: {e}")
        return
    if 'GPS' not in exif_dict:
        print(f"No GPS data found in: {file_name}")
        return
    exif_dict['GPS'][2] = adjust_gps_coordinate(original_gps_data['GPS'][2], random.randint(-99, 99))
    exif_dict['GPS'][4] = adjust_gps_coordinate(original_gps_data['GPS'][4], random.randint(-99, 99))
    exif_dict['GPS'][6] = original_gps_data['GPS'][6]
    print(f"Updated GPS data for {file_name}: {exif_dict['GPS'][2]}, {exif_dict['GPS'][4]}, {exif_dict['GPS'][6]}")
    try:
        exif_bytes = piexif.dump(exif_dict)
        img.save(file_name, "jpeg", exif=exif_bytes)
    except Exception as e:
        print(f"Error saving {file_name}: {e}")
def adjust_gps_data(directory, image_path):
    original_exif = load_exif_data(image_path)
    if original_exif is None or 'GPS' not in original_exif:
        print(f"No valid GPS data found in: {image_path}")
        return
    os.chdir(directory)
    files = os.listdir(directory)
    for file_name in files:
        update_image_gps_data(file_name, original_exif)
if __name__ == "__main__":
    reference_image = input("Enter the name of the reference image: ")
    directory = input("Enter the name of the directory: ")
    adjust_gps_data(directory, reference_image)