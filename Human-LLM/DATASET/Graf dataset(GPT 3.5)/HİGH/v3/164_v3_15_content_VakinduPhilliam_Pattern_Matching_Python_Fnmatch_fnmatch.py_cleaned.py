import fnmatch
import os
b1 = '.'
for file_name in os.listdir(b1):
    if fnmatch.fnmatch(file_name, '*.txt'):
        print("Found a text file:", file_name)