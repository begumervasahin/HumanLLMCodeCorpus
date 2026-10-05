
import fnmatch
import os
directory_to_search = '.'
for filename in os.listdir(directory_to_search):
    if fnmatch.fnmatch(filename, '*.txt'):
        print("Found a text file:", filename)