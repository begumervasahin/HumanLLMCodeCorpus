import os
from PIL import Image
import piexif
from random import randint
def gpsch(directory, image_file):
    try:
        reference_exif = piexif.load(image_file)
        if reference_exif['GPS']:
            gps_latitude = reference_exif['GPS'][2]
            gps_longitude = reference_exif['GPS'][4]
            gps_altitude = reference_exif['GPS'][6]
            print(f"Latitude: {gps_latitude}")
            print(f"Longitude: {gps_longitude}")
            print(f"Altitude: {gps_altitude}")
        os.chdir(directory)
        files = os.listdir(directory)
        for filename in files:
            lat_offset = randint(-99, 99)
            lon_offset = randint(-99, 99)
            try:
                image = Image.open(filename)
                exif_dict = piexif.load(image.info["exif"])
                if 'GPS' in exif_dict:
                    if gps_latitude:
                        exif_dict['GPS'][2] = (
                            gps_latitude[0],
                            gps_latitude[1],
                            (gps_latitude[2][0] + lat_offset, gps_latitude[2][1])
                        )
                    if gps_longitude:
                        exif_dict['GPS'][4] = (
                            gps_longitude[0],
                            gps_longitude[1],
                            (gps_longitude[2][0] + lon_offset, gps_longitude[2][1])
                        )
                    if gps_altitude:
                        exif_dict['GPS'][6] = gps_altitude
                    print(f"Updated Latitude: {exif_dict['GPS'][2]}")
                    print(f"Updated Longitude: {exif_dict['GPS'][4]}")
                    print(f"Updated Altitude: {exif_dict['GPS'][6]}")
                    exif_bytes = piexif.dump(exif_dict)
                    image.save(filename, "jpeg", exif=exif_bytes)
            except Exception as e:
                print(f"Error processing file {filename}: {e}")
    except Exception as e:
        print(f"Error loading reference image {image_file}: {e}")
reference_image = input("Enter the reference image filename: ")
target_directory = input("Enter the target directory name: ")
gpsch(target_directory, reference_image)