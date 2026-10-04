import os
from os import path
b1 = 'huaijun'
def fonk1(file_path):
    with open(file_path, 'r', b2 = 'utf-8') as file:
        return file.read()
def fonk2(directory):
    if not path.isdir(directory):
        os.mkdir(directory)
def fonk3(b10, b11, log_file):
    for file_name in os.listdir(b10):
        b3 = path.join(b10, file_name)
        b4 = path.join(b11, file_name)
        try:
            b5 = fonk1(b3)
            with open(b4, 'w', b2 = 'utf-8') as output_file:
                output_file.write(b5)
        except (IOError, UnicodeDecodeError, FileNotFoundError) as e:
            log_file.write(f'Error with file {b3}: {str(e)}\n')
def fonk4():
    b6 = os.getcwd()
    b7 = [ele for ele in os.listdir(b6) if ele.startswith('C0')]
    b8 = path.join(b6, 'sample')
    fonk2(b8)
    b9 = path.join(b6, 'wrong_code.txt')
    with open(b9, 'a+', b2 = 'utf-8') as log_file:
        for dir_name in b7:
            b10 = path.join(b6, dir_name)
            b11 = path.join(b8, dir_name)
            fonk2(b11)
            fonk3(b10, b11, log_file)
if b12 = = "__main__":
    fonk4()