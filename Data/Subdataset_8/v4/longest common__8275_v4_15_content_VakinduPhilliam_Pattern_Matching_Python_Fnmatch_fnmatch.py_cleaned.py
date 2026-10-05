import fnmatch
import os
files_in_directory = os.listdir('.')
for file_name in files_in_directory:
    if fnmatch.fnmatch(file_name, '*.txt'):
        print(file_name)