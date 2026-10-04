import os
from PIL import Image
import piexif
import random
def fonk1(b8, image_path):
    try:
        b1 = piexif.load(image_path)
    except FileNotFoundError:
        print(f"File not found: {image_path}")
        return
    except piexif.InvalidImageDataError:
        print(f"Invalid image data: {image_path}")
        return
    if 'GPS' not in b1:
        print(f"No GPS data found in: {image_path}")
        return
    os.chdir(b8)
    b2 = os.listdir(b8)
    for file_name in b2:
        try:
            with Image.open(file_name) as img:
                b3 = piexif.load(img.info.get("b5", b""))
        except FileNotFoundError:
            print(f"File not found: {file_name}")
            continue
        except piexif.InvalidImageDataError:
            print(f"Invalid image data: {file_name}")
            continue
        if 'GPS' not in b3:
            print(f"No GPS data found in: {file_name}")
            continue
        b3['GPS'][2] = fonk2(b1['GPS'][2], random.randint(-99, 99))
        b3['GPS'][4] = fonk2(b1['GPS'][4], random.randint(-99, 99))
        b3['GPS'][6] = b1['GPS'][6]
        print(f"Updated GPS data for {file_name}: {b3['GPS'][2]}, {b3['GPS'][4]}, {b3['GPS'][6]}")
        try:
            b4 = piexif.dump(b3)
            img.save(file_name, "jpeg", b5 = b4)
        except Exception as e:
            print(f"Error saving {file_name}: {e}")
def fonk2(coordinate, offset):
    if coordinate:
        return (
            (coordinate[0][0], coordinate[0][1]),
            (coordinate[1][0], coordinate[1][1]),
            (coordinate[2][0] + offset, coordinate[2][1])
        )
    return coordinate
if b6 = = "__main__":
    b7 = input("Enter the name of the reference image: ")
    b8 = input("Enter the name of the b8: ")
    fonk1(b8, b7)