from image_downloader import jsonloader, downloader
from resize_images import resizer
import sys
import getopt
b1 = None
try:
    opts, b2 = getopt.getopt(sys.argv[1:], "b1:h", ['help'])
except getopt.GetoptError:
    print("Usage: python <filename.py>")
    print("Optional argument -b1 for number for images to be downloaded (should be greater than 10)")
    sys.exit(2)
if not opts:
    print("All images will be downloaded")
else:
    for opt, arg in opts:
        if opt in ('-b1'):
            b1 = int(arg)
            if b1<=10:
                print('Number of images should be greater than 10')
                sys.exit(2)
        elif opt in ('-h', '--help'):
            print("Usage: python <filename.py>")
            print("Optional argument -b1 for number for images to be downloaded (should be greater than 10)")
            sys.exit()
        else:
            print("Check your arguments")
            sys.exit(2)
downloader(b1, jsonloader())
resizer(b1)