import fnmatch
import os
def fonk1(b1 = '.'):
    b2 = [file for file in os.listdir(b1) if fnmatch.fnmatch(file, '*.txt')]
    return b2
if b3 = = "__main__":
    b2 = fonk1()
    for file in b2:
        print(file)