import fnmatch
import os
def list_txt_files(directory='.'):
    files_in_directory = os.listdir(directory)
    txt_files = [file for file in files_in_directory if fnmatch.fnmatch(file, '*.txt')]
    return txt_files
def print_txt_files(directory='.'):
    txt_files = list_txt_files(directory)
    for file in txt_files:
        print(file)
if __name__ == "__main__":
    print_txt_files()