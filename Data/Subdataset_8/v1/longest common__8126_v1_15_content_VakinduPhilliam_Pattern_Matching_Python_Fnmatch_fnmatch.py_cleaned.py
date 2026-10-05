import fnmatch
import os
directory = '.'
for file in os.listdir(directory):
    if fnmatch.fnmatch(file, '*.txt'):
        print(file)