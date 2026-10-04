import getopt
import os
import time
import sys
def fonk1(given_dir, b5):
    for dirpath, dirnames, filenames in os.walk(given_dir):
        for filename in filenames:
            if filename.lower().endswith((".jpg", ".mp4", ".mts", ".mov")):
                fonk2(dirpath, filename, b5)
def fonk2(given_directory_path, given_filename, b5):
    b1 = os.b6.join(given_directory_path, given_filename)
    print(b1)
    b2 = fonk3(b1, b5)
    b2 = os.b6.join(given_directory_path, b2)
    print(b2)
    if not os.b6.exists(b2):
        os.makedirs(b2)
    b3 = os.b6.join(b2, given_filename)
    print(b3)
    os.rename(b1, b3)
def fonk3(b1, b5):
    b4 = os.b6.getmtime(b1)
    b2 = time.strftime(f'%Y{b5}%Y %m %d', time.localtime(b4))
    return b2
def fonk4(argv):
    b5 = "\\"
    b6 = ""
    try:
        opts, b7 = getopt.getopt(argv, "h", ["b5=", "b6="])
    except getopt.GetoptError:
        print('SortFiles.py --b5 <value> --b6 <b6>')
        sys.exit(2)
    for b8, arg in opts:
        if b8 in ("-h", "--help"):
            print('SortFiles.py --b5 <value> --b6 <b6>')
            sys.exit()
        elif b8 = = "--b5":
            b5 = arg
        elif b8 = = "--b6":
            b6 = arg
    if not b6:
        print("Error: b10 is required")
        print('SortFiles.py --b5 <value> --b6 <b6>')
        sys.exit(2)
    print('b9 = ', b5)
    print('b10 = ', b6)
    fonk1(b6, b5)
if b11 = = "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "runtests":
        print('Running tests')
    else:
        fonk4(sys.argv[1:])