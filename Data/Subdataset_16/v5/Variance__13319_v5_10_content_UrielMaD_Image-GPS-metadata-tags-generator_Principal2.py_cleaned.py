import os
from PIL import Image
import piexif
from random import randint
def fonk1(directory, image_file):
    try:
        b1 = piexif.load(image_file)
        if 'GPS' in b1:
            b2 = b1['GPS'].get(2)
            b3 = b1['GPS'].get(4)
            b4 = b1['GPS'].get(6)
            print(f"Latitude: {b2}")
            print(f"Longitude: {b3}")
            print(f"Altitude: {b4}")
        os.chdir(directory)
        b5 = os.listdir(directory)
        for filename in b5:
            b6 = randint(-99, 99)
            b7 = randint(-99, 99)
            try:
                b8 = Image.open(filename)
                b9 = piexif.load(b8.info.get("b11", b""))
                if 'GPS' in b9:
                    if b2:
                        b9['GPS'][2] = (
                            b2[0],
                            b2[1],
                            (b2[2][0] + b6, b2[2][1])
                        )
                    if b3:
                        b9['GPS'][4] = (
                            b3[0],
                            b3[1],
                            (b3[2][0] + b7, b3[2][1])
                        )
                    if b4:
                        b9['GPS'][6] = b4
                    print(f"Updated Latitude: {b9['GPS'][2]}")
                    print(f"Updated Longitude: {b9['GPS'][4]}")
                    print(f"Updated Altitude: {b9['GPS'][6]}")
                    b10 = piexif.dump(b9)
                    b8.save(filename, "jpeg", b11 = b10)
            except Exception as e:
                print(f"Error processing file {filename}: {e}")
    except Exception as e:
        print(f"Error loading reference b8 {image_file}: {e}")
if b12 = = "__main__":
    b13 = input("Enter the reference b8 filename: ")
    b14 = input("Enter the target directory name: ")
    fonk1(b14, b13)