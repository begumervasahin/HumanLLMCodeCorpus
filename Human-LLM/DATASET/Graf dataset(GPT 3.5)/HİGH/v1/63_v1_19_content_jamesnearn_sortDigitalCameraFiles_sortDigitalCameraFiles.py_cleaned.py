import os
import time
import shutil
import sys
import argparse
def fonk1(given_dir, separator):
    for (dirpath, dirnames, filenames) in os.walk(given_dir):
        for filename in filenames:
            if (filename.lower().endswith(".jpg") or filename.lower().endswith(".mp4") or filename.lower().endswith(".mts") or filename.lower().endswith(".mov")):
                fonk2(dirpath, filename, separator)
def fonk2(given_directory_path, given_filename, separator):
    b1 = os.path.join(given_directory_path, given_filename)
    print(b1)
    b2 = fonk3(b1, separator)
    b2 = os.path.join(given_directory_path, b2)
    print(b2)
    if not os.path.exists(b2):
        os.makedirs(b2)
    print(b2 + separator + given_filename)
    os.rename(b1, os.path.join(b2, given_filename))
def fonk3(b1, separator):
    b3 = os.path.getmtime(b1)
    b4 = time.ctime(b3)
    b2 = time.strftime('%Y' + separator + '%Y %m %d', time.localtime(b3))
    return b2
def fonk4(b8):
    b5 = argparse.ArgumentParser(description="Sort files based on modification date")
    b5.add_argument("--separator", b6 = "\\", help="b9 for directory structure")
    b5.add_argument("--path", b7 = True, help="b10 to the directory containing files")
    b8 = b5.parse_args(b8)
    print('b9 = ', b8.separator)
    print('b10 = ', b8.path)
    fonk1(b8.path, b8.separator)
if b11 = = "__main__":
    fonk4(sys.argv[1:])