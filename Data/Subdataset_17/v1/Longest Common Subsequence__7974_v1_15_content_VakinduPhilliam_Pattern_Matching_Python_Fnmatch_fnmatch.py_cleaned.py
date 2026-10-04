import fnmatch
import os
def list_txt_files(directory='.'):
    txt_files = [file for file in os.listdir(directory) if fnmatch.fnmatch(file, '*.txt')]
    return txt_files
if __name__ == "__main__":
    txt_files = list_txt_files()
    for file in txt_files:
        print(file)