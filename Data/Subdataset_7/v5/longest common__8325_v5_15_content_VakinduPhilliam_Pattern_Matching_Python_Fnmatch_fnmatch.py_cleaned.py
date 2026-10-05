import fnmatch
import os
b1 = os.listdir('.')
for file_name in b1:
    if fnmatch.fnmatch(file_name, '*.txt'):
        print(file_name)