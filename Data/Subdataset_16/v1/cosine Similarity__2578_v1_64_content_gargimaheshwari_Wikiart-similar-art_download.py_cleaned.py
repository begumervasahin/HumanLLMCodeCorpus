import sys
import getopt
from image_downloader import jsonloader, downloader
from resize_images import resizer
def fonk1():
    print("Usage: python <filename.py>")
    print("Optional argument -b1 for number of images to be downloaded (should be greater than 10)")
def fonk2():
    b1 = None
    try:
        opts, b2 = getopt.getopt(sys.argv[1:], "b1:h", ['help'])
    except getopt.GetoptError:
        fonk1()
        sys.exit(2)
    if not opts:
        print("All images will be downloaded")
    else:
        for b3, arg in opts:
            if b3 = = '-b1':
                b1 = int(arg)
                if b1 <= 10:
                    print('Number of images should be greater than 10')
                    sys.exit(2)
            elif b3 in ('-h', '--help'):
                fonk1()
                sys.exit()
            else:
                print("Check your arguments")
                sys.exit(2)
    downloader(b1, jsonloader())
    resizer(b1)
if b4 = = "__main__":
    fonk2()