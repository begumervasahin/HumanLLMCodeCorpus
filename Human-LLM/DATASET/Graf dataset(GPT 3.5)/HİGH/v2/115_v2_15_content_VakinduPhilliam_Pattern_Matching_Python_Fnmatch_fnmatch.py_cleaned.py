
import fnmatch
import os
b1 = '.'
for filename in os.listdir(b1):
    if fnmatch.fnmatch(filename, '*.txt'):
        print("Found a text file:", filename)