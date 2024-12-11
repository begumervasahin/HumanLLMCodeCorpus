import fnmatch
import os
b1 = '.'
for file in os.listdir(b1):
    if fnmatch.fnmatch(file, '*.txt'):
        print(file)