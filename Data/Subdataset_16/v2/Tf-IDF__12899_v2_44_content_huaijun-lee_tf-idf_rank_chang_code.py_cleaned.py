import os
from os import path
b1 = 'huaijun'
def fonk1(file):
    try:
        with open(file, 'r', b2 = 'utf-8') as file_handle:
            b3 = file_handle.read()
        return b3
    except Exception as e:
        raise e
def fonk2():
    b4 = os.getcwd()
    b5 = os.listdir(b4)
    b6 = [d for d in b5 if d.startswith('C0')]
    b7 = path.join(b4, 'sample')
    if not path.isdir(b7):
        os.mkdir(b7)
    with open(path.join(b4, 'wrong_code.txt'), 'a+', b2 = 'utf-8') as log_file:
        for directory in b6:
            b8 = path.join(b7, directory)
            if not path.isdir(b8):
                os.mkdir(b8)
            b9 = path.join(b4, directory)
            b10 = os.listdir(b9)
            for file_name in b10:
                b11 = path.join(b9, file_name)
                try:
                    b3 = fonk1(b11)
                    with open(path.join(b8, file_name), 'w', b2 = 'utf-8') as new_file:
                        new_file.write(b3)
                except (IOError, UnicodeDecodeError, FileNotFoundError) as e:
                    log_file.write(f'Error processing {directory}/{file_name}: {str(e)}\n')
if b12 = = "__main__":
    fonk2()