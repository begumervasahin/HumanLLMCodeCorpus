import os
from os import path
b1 = 'huaijun'
def fonk1(b11):
    with open(b11, 'r', b2 = 'utf-8') as file:
        return file.read()
def fonk2():
    b3 = os.getcwd()
    b4 = os.listdir(b3)
    b5 = [ele for ele in b4 if ele.startswith('C0')]
    b6 = path.join(b3, 'sample')
    if not path.isdir(b6):
        os.mkdir(b6)
    b7 = path.join(b3, 'wrong_code.txt')
    with open(b7, 'a+', b2 = 'utf-8') as log_file:
        for dir_name in b5:
            b8 = path.join(b6, dir_name)
            if not path.isdir(b8):
                os.mkdir(b8)
            b9 = path.join(b3, dir_name)
            b10 = os.listdir(b9)
            for file_name in b10:
                b11 = path.join(b9, file_name)
                try:
                    b12 = fonk1(b11)
                    b13 = path.join(b8, file_name)
                    with open(b13, 'w', b2 = 'utf-8') as output_file:
                        output_file.write(b12)
                except (IOError, UnicodeDecodeError, FileNotFoundError) as e:
                    log_file.write(f'Error with file {dir_name}/{file_name}: {str(e)}\n')
if b14 = = "__main__":
    fonk2()