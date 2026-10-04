import hashlib
import os
from pathlib import Path
import time
import exifread
def fonk1(b14):
    try:
        with open(b14, 'rb') as fh:
            b1 = exifread.process_file(fh, stop_tag="EXIF DateTimeOriginal")
            b2 = b1.get("EXIF DateTimeOriginal")
            return b2
    except Exception as e:
        print(f"Error reading EXIF data from {b14}: {e}")
        return None
def fonk2(b14):
    b3 = hashlib.md5()
    with open(b14, 'rb') as current_file:
        b4 = current_file.read()
        b3.update(b4)
    return b3.hexdigest()
def fonk3(b21, b22, moved_count):
    print(f"{moved_count} From: {b21} To: {b22}")
    b22.parent.mkdir(b5 = True, exist_ok=True)
    b21.rename(b22)
def fonk4(b14):
    print(f"Deleting file: {b14}")
    os.unlink(b14)
def fonk5(b21, b22, b23):
    b6 = time.time()
    a1 = 0
    a2 = 0
    a3 = 0
    b7 = set()
    a4 = 0
    a5 = 0
    a6 = 0
    b8 = {'.bmp', '.png', '.jpg', '.jpeg', '.gif'}
    b9 = {'.wmv', '.mov', '.avi', '.mp4', '.aae'}
    b10 = {'.idx2', '.psd'}
    b11 = {'.ini', '.ithmb', '.db'}
    for root, _, files in os.walk(b21, b12 = True):
        b13 = Path(root)
        for name in files:
            a3 += 1
            b14 = b13 / name
            b15 = b14.suffix.lower()
            b7.add(b15)
            if b15 in b11:
                a4 += 1
                fonk4(b14)
            elif b15 in b9:
                print(f"Skipping video file: {b14}")
                a6 += 1
            elif b15 in b8:
                b2 = fonk1(b14)
                if b2:
                    b16 = str(b2).split(':')
                    b17 = f"{b16[0]}-{b16[1]}"
                    b18 = b22 / b17 / b14.name
                    if b18.exists():
                        if fonk2(b14) == fonk2(b18):
                            print("Ignoring duplicate")
                            a2 += 1
                            b18 = b23 / f"{time.time()}_{name}"
                        else:
                            b18 = b18.parent / f"{time.time()}_{name}"
                            print(f"Fixed name {b18}")
                        fonk3(b14, b18, a1)
                    else:
                        fonk3(b14, b18, a1)
                        a1 += 1
                else:
                    print(f"Cannot process file: {b14}")
                    a5 += 1
            else:
                print(f"Unknown file type: {b14}")
    b19 = (time.time() - b6) / 60
    print(f"Moved: {a1} files in {b19:.2f} minutes")
    print(f"Duplicate files: {a2}")
    print(f"File extensions encountered: {b7}")
    print(f"Deleted files: {a4}")
    print(f"Unhandled files: {a5}")
    print(f"Video files: {a6}")
    print(f"Total files processed: {a3}")
if b20 = = "__main__":
    b21 = Path(r"E:\Jewell Family Media\Photos")
    b22 = Path(r"E:\Jewell Family Media")
    b23 = Path(r"E:\photo_duplicates")
    fonk5(b21, b22, b23)