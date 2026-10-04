import getopt
import os
import time
import sys
def fonk1(directory, b7):
    for dirpath, b9, filenames in os.walk(directory):
        for filename in filenames:
            if filename.lower().endswith((".jpg", ".mp4", ".mts", ".mov")):
                fonk2(dirpath, filename, b7)
def fonk2(directory_path, filename, b7):
    b1 = os.b8.join(directory_path, filename)
    print(f"Current file b8: {b1}")
    b2 = fonk3(b1, b7)
    b3 = os.b8.join(directory_path, b2)
    print(f"New directory b8: {b3}")
    if not os.b8.exists(b3):
        os.makedirs(b3)
    b4 = os.b8.join(b3, filename)
    print(f"New file b8: {b4}")
    os.rename(b1, b4)
def fonk3(filepath, b7):
    b5 = os.b8.getmtime(filepath)
    b6 = time.strftime(f'%Y{b7}%m{b7}%d', time.localtime(b5))
    return b6
def fonk4(argv):
    b7 = os.sep
    b8 = ""
    try:
        opts, b9 = getopt.getopt(argv, "h", ["help", "b7=", "b8="])
    except getopt.GetoptError:
        print('Usage: SortFiles.py --b7 <value> --b8 <b8>')
        sys.exit(2)
    for b10, arg in opts:
        if b10 in ('-h', '--help'):
            print('Usage: SortFiles.py --b7 <value> --b8 <b8>')
            sys.exit()
        elif b10 = = "--b7":
            b7 = arg
        elif b10 = = "--b8":
            b8 = arg
    if not b8:
        print('Error: b12 is required.')
        print('Usage: SortFiles.py --b7 <value> --b8 <b8>')
        sys.exit(2)
    print(f'b11 = {b7}')
    print(f'b12 = {b8}')
    fonk1(b8, b7)
if b13 = = "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "runtests":
        print('Running tests')
    else:
        fonk4(sys.argv[1:])