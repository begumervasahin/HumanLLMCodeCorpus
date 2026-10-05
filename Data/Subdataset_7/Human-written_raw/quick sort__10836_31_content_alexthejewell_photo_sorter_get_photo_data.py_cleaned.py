import hashlib
import os
from pathlib import Path
import time
import exifread as exifread
def fonk1(b18):
    try:
        with open(str(b18), 'rb') as fh:
            b1 = exifread.process_file(fh, stop_tag="EXIF DateTimeOriginal")
            b2 = b1["EXIF DateTimeOriginal"]
            return b2
    except:
        return None
def fonk2(b18):
    b3 = hashlib.md5()
    with open(str(b18), 'rb') as current_file:
        b4 = current_file.read()
        b3.update(b4)
    return b3.hexdigest()
def fonk3(b7, b8, moved_count):
    print("{} From: {} To: {}".format(moved_count, b18, b22))
    if not b8.parent.exists():
        b8.parent.mkdir(b5 = True)
    b7.rename(b8)
def fonk4(b18):
    print("Deleting file: {}".format(b18))
    os.unlink(str(b18))
if b6 = = "__main__":
    b7 = Path(r"E:\Jewell Family Media\Photos")
    b8 = Path(r"E:\Jewell Family Media")
    b9 = Path(r"E:\photo_duplicates")
    b10 = time.time()
    a1 = 0
    a2 = 0
    a3 = 0
    b11 = set()
    a4 = 0
    a5 = 0
    a6 = 0
    b12 = ['.bmp', '.png', '.jpg', '.JPG', '.PNG', '.GIF', '.jpeg']
    b13 = ['.wmv', '.MOV', '.AVI', '.AAE', '.mov', '.mp4']
    b14 = ['.idx2', '.psd']
    b15 = ['.ini', '.ithmb', '.db']
    for root, dirs, files in os.walk(str(b7), b16 = True):
        b17 = Path(root)
        for name in files:
            a3 += 1
            b18 = b17 / name
            b19 = b18.suffix
            b11.add(b19)
            if b19 in b15:
                a4 += 1
                fonk4(b18)
            elif b19 in b13:
                print("Skipping video file: {}".format(b18))
                a6 += 1
            elif b19 in b12:
                b2 = fonk1(b18)
                if b2:
                    b20 = b2.values.split(':')
                    b21 = "{}-{}".format(b20[0], b20[1])
                    b22 = b8 / b21 / b18.name
                    if b22.exists():
                        if fonk2(b18) == fonk2(b22):
                            print("Ignoring duplicate")
                            a2 += 1
                            b22 = b9 / "{}_{}".format(time.time(), name)
                            fonk3(b18, b22, a1)
                        else:
                            b22 = b22.parent / "{}_{}".format(time.time(), name)
                            print("Fixed name {}".format(b22))
                            a1 += 1
                            fonk3(b18, b22, a1)
                    else:
                        fonk3(b18, b22, a1)
                        a1 += 1
                else:
                    print("Cannot process file: {}".format(b18))
                    a5 += 1
            else:
                print("Uknown file type: {}".format(b18))
    print("Moved: {} files in {} minutes".format(a1, (time.time() - b10)/60))
    print("Duplicate files {}".format(a2))
    print("File extensions encountered: {}".format(b11))
    print("Deleted files: {}".format(a4))
    print("Unhandled files: {}".format(a5))
    print("Video files: {}".format(a6))
    print("Total: {}".format(a3))