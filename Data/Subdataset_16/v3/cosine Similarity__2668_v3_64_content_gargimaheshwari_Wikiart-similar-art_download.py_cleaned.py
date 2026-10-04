import sys
import getopt
from image_downloader import jsonloader, downloader
from resize_images import resizer
def fonk1():
    print("Usage: python <filename.py>")
    print("Optional argument -b2 for number of images to be downloaded (should be greater than 10)")
def fonk2():
    try:
        opts, b1 = getopt.getopt(sys.argv[1:], "b2:h", ["help"])
    except getopt.GetoptError:
        fonk1()
        sys.exit(2)
    b2 = None
    for b3, arg in opts:
        if b3 = = '-b2':
            b2 = int(arg)
            if b2 <= 10:
                print('Number of images should be greater than 10')
                sys.exit(2)
        elif b3 in ('-h', '--help'):
            fonk1()
            sys.exit()
        else:
            print("Check your arguments")
            sys.exit(2)
    return b2
def fonk3():
    b2 = fonk2()
    if b2 is None:
        print("All images will be downloaded")
    downloader(b2, jsonloader())
    resizer(b2)
if b4 = = "__main__":
    fonk3()