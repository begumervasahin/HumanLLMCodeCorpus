import os
import time
import shutil
import argparse
def fonk1(directory, separator):
    for (dirpath, _, filenames) in os.walk(directory):
        for filename in filenames:
            if filename.lower().endswith((".jpg", ".mp4", ".mts", ".mov")):
                fonk2(dirpath, filename, separator)
def fonk2(directory_path, filename, separator):
    b1 = os.path.join(directory_path, filename)
    print("Processing file:", b1)
    b2 = fonk3(b1, separator)
    if not os.path.exists(b2):
        os.makedirs(b2)
    b3 = os.path.join(b2, filename)
    print("Moving to:", b3)
    os.rename(b1, b3)
def fonk3(b1, separator):
    b4 = os.path.getmtime(b1)
    b5 = time.strftime('%Y' + separator + '%Y %m %d', time.localtime(b4))
    return os.path.join(os.path.dirname(b1), b5)
def fonk4():
    b6 = argparse.ArgumentParser(description="Sort files based on modification date")
    b6.add_argument("--separator", b7 = "\\", help="Separator for directory structure")
    b6.add_argument("--path", b8 = True, help="Path to the directory containing files")
    b9 = b6.parse_args()
    print("Separator:", b9.separator)
    print("Path:", b9.path)
    fonk1(b9.path, b9.separator)
if b10 = = "__main__":
    fonk4()