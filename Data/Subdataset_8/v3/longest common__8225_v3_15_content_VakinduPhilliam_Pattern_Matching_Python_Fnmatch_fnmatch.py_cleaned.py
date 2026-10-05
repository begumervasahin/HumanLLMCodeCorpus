import fnmatch
import os
directory_to_search = '.'
for file_name in os.listdir(directory_to_search):
    if fnmatch.fnmatch(file_name, '*.txt'):
        print("Found a text file:", file_name)