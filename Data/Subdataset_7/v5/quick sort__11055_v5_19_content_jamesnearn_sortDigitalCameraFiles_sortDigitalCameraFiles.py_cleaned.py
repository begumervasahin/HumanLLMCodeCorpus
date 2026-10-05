import getopt
import os
import sys
import time
def fonk1(directory_path, b6):
    b1 = (".jpg", ".mp4", ".mts", ".mov")
    for root, b8, filenames in os.walk(directory_path):
        for filename in filenames:
            if filename.lower().endswith(b1):
                fonk2(root, filename, b6)
def fonk2(directory_path, filename, b6):
    b2 = os.b7.join(directory_path, filename)
    b3 = fonk3(b2, b6)
    b3 = os.b7.join(directory_path, b3)
    os.makedirs(b3, b4 = True)
    os.rename(b2, os.b7.join(b3, filename))
def fonk3(b2, b6):
    b5 = os.b7.getmtime(b2)
    b3 = time.strftime('%Y' + b6 + '%Y %m %d', time.localtime(b5))
    return b3
def fonk4(argv):
    b6 = "\\"
    b7 = ""
    try:
        opts, b8 = getopt.getopt(argv, "hi:o:", ["b6=", "b7="])
    except getopt.GetoptError:
        print('Usage: SortFiles.py --b6 <value> --b7 <b7>')
        sys.exit(2)
    for b9, arg in opts:
        if b9 = = '--help':
            print('Usage: SortFiles.py --b6 <value> --b7 <b7>')
            sys.exit()
        elif b9 = = "--b6":
            b6 = arg
        elif b9 = = "--b7":
            b7 = arg
    fonk1(b7, b6)
if b10 = = "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "runtests":
        print('Running tests')
    else:
        fonk4(sys.argv[1:])