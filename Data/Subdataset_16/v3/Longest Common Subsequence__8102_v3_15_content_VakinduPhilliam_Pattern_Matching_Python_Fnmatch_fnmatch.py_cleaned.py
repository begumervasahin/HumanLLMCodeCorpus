import fnmatch
import os
def fonk1(b1 = '.'):
    b2 = os.listdir(b1)
    b3 = [file for file in b2 if fnmatch.fnmatch(file, '*.txt')]
    return b3
def fonk2(b1 = '.'):
    b3 = fonk1(b1)
    for file in b3:
        print(file)
if b4 = = "__main__":
    fonk2()