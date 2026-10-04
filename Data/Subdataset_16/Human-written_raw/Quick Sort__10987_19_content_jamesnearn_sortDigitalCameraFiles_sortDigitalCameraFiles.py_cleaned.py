import getopt
import os
import time
import shutil
import sys
def fonk1(givendir, b5):
    for (dirpath, dirnames, filenames) in os.walk(givendir):
        for filename in filenames:
            if (filename.lower().endswith(".jpg") or filename.lower().endswith(".mp4") or filename.lower().endswith(".mts") or filename.lower().endswith(".mov")):
                fonk2(dirpath, filename, b5)
def fonk2(givenDirectoryPath, givenFilename, b5):
    b1 = os.b6.join(givenDirectoryPath, givenFilename)
    print(b1)
    b2 = fonk3(b1, b5)
    b2 = os.b6.join(givenDirectoryPath, b2)
    print(b2)
    if not os.b6.exists(b2):
        os.makedirs(b2)
    print(b2 + b5 + givenFilename)
    os.rename(b1, b2 + b5 + givenFilename)
def fonk3(b1, b5):
    b3 = os.b6.getmtime(b1)
    b4 = time.ctime(b3)
    b2 = time.strftime('%Y' + b5 + '%Y %m %d', time.localtime(b3))
    return b2
def fonk4(argv):
    b5 = "\\"
    b6 = ""
    try:
        opts, b7 = getopt.getopt(argv,"hi:o:",["b5=","b6="])
    except getopt.GetoptError:
        print('SortFiles.py --b5 <value> --b6 <b6>')
        print('Number of arguments:', len(sys.argv), 'arguments.')
        print('Argument List:', str(sys.argv))
        sys.exit(2)
    for b8, arg in opts:
        if b8 = = '--help':
            print('SortFiles.py --b5 <value> --b6 <b6>')
            sys.exit()
        elif b8 in ("--b5"):
            b5 = arg
        elif b8 in ("--b6"):
            b6 = arg
    print('b9 = ', b5)
    print('b10 = ', b6)
    fonk1(b6, b5)
if b11 = = "__main__":
    if (sys.argv[1] == "runtests"):
        print('Running tests')
    else:
        fonk4(sys.argv[1:])