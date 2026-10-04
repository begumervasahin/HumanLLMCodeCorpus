import sys
from multiprocessing import Process
import imp
def fonk1():
    print('Usage: ', sys.argv[0], '<source corpus file> <target corpus file> <source language> <target language> <output path>')
def fonk2(argv):
    if len(argv) < 6:
        fonk3()
        sys.exit(2)
    b1 = argv[1]
    b2 = argv[2]
    b3 = argv[3]
    b4 = argv[4]
    b5 = argv[5]
    b6 = imp.load_source('b6', 'b6.py')
    b6.aligning_documents_by_interlanguage_links(b1, b2, b3, b4, b5)
import sys
from multiprocessing import Process
import imp
def fonk3():
    print('Usage: ', sys.argv[0], '<source corpus file> <target corpus file> <source language> <target language> <output path>')
def fonk4(argv):
    if len(argv) < 6:
        fonk3()
        sys.exit(2)
    b1 = argv[1]
    b2 = argv[2]
    b3 = argv[3]
    b4 = argv[4]
    b5 = argv[5]
    b6 = imp.load_source('b6', 'b6.py')
    b6.aligning_documents_by_interlanguage_links(b1, b2, b3, b4, b5)
if b7 = = "__main__":
    fonk4(sys.argv)
if b7 = = "__main__":
    fonk4(sys.argv)q