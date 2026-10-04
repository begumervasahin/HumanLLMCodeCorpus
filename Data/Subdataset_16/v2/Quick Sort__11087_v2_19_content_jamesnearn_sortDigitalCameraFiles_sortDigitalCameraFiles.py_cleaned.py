import getopt
import os
import time
import sys
def fonk1(b7, b6):
    for dirpath, dirnames, filenames in os.walk(b7):
        for filename in filenames:
            if filename.lower().endswith((".jpg", ".mp4", ".mts", ".mov")):
                fonk2(dirpath, filename, b6)
def fonk2(directory_path, filename, b6):
    b1 = os.path.join(directory_path, filename)
    print(f"Processing file: {b1}")
    b2 = fonk3(b1, b6)
    b3 = os.path.join(directory_path, b2)
    print(f"Destination b7: {b3}")
    if not os.path.exists(b3):
        os.makedirs(b3)
    b4 = os.path.join(b3, filename)
    print(f"Moving file to: {b4}")
    os.rename(b1, b4)
def fonk3(filepath, b6):
    b5 = os.path.getmtime(filepath)
    b2 = time.strftime(f'%Y{b6}%Y %m %d', time.localtime(b5))
    return b2
def fonk4(argv):
    b6 = os.sep
    b7 = ""
    try:
        opts, b8 = getopt.getopt(argv, "h", ["b6=", "path="])
    except getopt.GetoptError:
        print('Usage: SortFiles.py --b6 <value> --path <path>')
        sys.exit(2)
    for b9, arg in opts:
        if b9 in ("-h", "--help"):
            print('Usage: SortFiles.py --b6 <value> --path <path>')
            sys.exit()
        elif b9 = = "--b6":
            b6 = arg
        elif b9 = = "--path":
            b7 = arg
    if not b7:
        print("Error: Path is required")
        print('Usage: SortFiles.py --b6 <value> --path <path>')
        sys.exit(2)
    print(f'Separator: {b6}')
    print(f'Path: {b7}')
    fonk1(b7, b6)
if b10 = = "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "runtests":
        print('Running tests')
    else:
        fonk4(sys.argv[1:])