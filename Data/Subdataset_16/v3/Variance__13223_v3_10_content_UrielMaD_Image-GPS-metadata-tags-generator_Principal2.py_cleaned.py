import os
from PIL import Image
import piexif
import random
def fonk1(image_path):
    try:
        return piexif.load(image_path)
    except (FileNotFoundError, piexif.InvalidImageDataError) as e:
        print(f"Error loading EXIF data from {image_path}: {e}")
        return None
def fonk2(coordinate, offset):
    if coordinate:
        return (
            (coordinate[0][0], coordinate[0][1]),
            (coordinate[1][0], coordinate[1][1]),
            (coordinate[2][0] + offset, coordinate[2][1])
        )
    return coordinate
def fonk3(file_name, original_gps_data):
    try:
        with Image.open(file_name) as img:
            b1 = piexif.load(img.info.get("b3", b""))
    except (FileNotFoundError, piexif.InvalidImageDataError) as e:
        print(f"Error loading EXIF data from {file_name}: {e}")
        return
    if 'GPS' not in b1:
        print(f"No GPS data found in: {file_name}")
        return
    b1['GPS'][2] = fonk2(original_gps_data['GPS'][2], random.randint(-99, 99))
    b1['GPS'][4] = fonk2(original_gps_data['GPS'][4], random.randint(-99, 99))
    b1['GPS'][6] = original_gps_data['GPS'][6]
    print(f"Updated GPS data for {file_name}: {b1['GPS'][2]}, {b1['GPS'][4]}, {b1['GPS'][6]}")
    try:
        b2 = piexif.dump(b1)
        img.save(file_name, "jpeg", b3 = b2)
    except Exception as e:
        print(f"Error saving {file_name}: {e}")
def fonk4(b8, image_path):
    b4 = fonk1(image_path)
    if b4 is None or 'GPS' not in b4:
        print(f"No valid GPS data found in: {image_path}")
        return
    os.chdir(b8)
    b5 = os.listdir(b8)
    for file_name in b5:
        fonk3(file_name, b4)
if b6 = = "__main__":
    b7 = input("Enter the name of the reference image: ")
    b8 = input("Enter the name of the b8: ")
    fonk4(b8, b7)