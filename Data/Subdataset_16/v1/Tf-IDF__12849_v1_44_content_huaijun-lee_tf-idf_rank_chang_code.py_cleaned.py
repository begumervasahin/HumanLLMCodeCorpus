import os
from os import path
b1 = 'huaijun'
def fonk1(file):
    try:
        with open(file, 'r', b2 = 'utf-8') as f_h:
            b3 = f_h.read()
        return b3
    except Exception as e:
        raise e
def fonk2():
    b4 = os.getcwd()
    b5 = os.listdir(b4)
    b6 = [ele for ele in b5 if ele.startswith('C0')]
    b7 = path.join(b4, 'sample')
    if not path.isdir(b7):
        os.mkdir(b7)
    with open(path.join(b4, 'wrong_code.txt'), 'a+', b2 = 'utf-8') as log_f:
        for dir in b6:
            b8 = path.join(b7, dir)
            if not path.isdir(b8):
                os.mkdir(b8)
            b9 = path.join(b4, dir)
            b10 = os.listdir(b9)
            for name in b10:
                try:
                    b11 = fonk1(path.join(b9, name))
                    with open(path.join(b8, name), 'w', b2 = 'utf-8') as w_f:
                        w_f.write(b11)
                except (IOError, UnicodeDecodeError, FileNotFoundError) as e:
                    log_f.write(f'éè¯¯çç¼ç  {dir} {name}\n')
if b12 = = "__main__":
    fonk2()
Q