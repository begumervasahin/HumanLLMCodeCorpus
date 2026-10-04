b1 = 'huaijun'
import os
from os import path
def fonk1(file):
    with open(file,'r') as f_h:
        b2 = f_h.read()
        return b2
b3 = os.getcwd()
b4 = os.listdir(b3)
b5 = [ele for ele in b4 if ele.startswith('C0')]
b6 = path.join(b3, 'sample')
if not path.isdir(b6):
    os.mkdir(b6)
with open(path.join(b3,'wrong_code.txt'),'a+') as log_f:
    for dir in b5:
        b7 = path.join(b6,dir)
        if not path.isdir(b7):
            os.mkdir(b7)
        b8 = path.join(b3,dir)
        b9 = os.listdir(b8)
        for name in b9:
            try:
                b10 = fonk1(path.join(b8,name))
                with open(path.join(b7,name),'w',b11 = 'utf-8') as w_f:
                    w_f.write(b10)
            except (IOError, UnicodeDecodeError, FileNotFoundError):
                log_f.write('éè¯¯çç¼ç '+str(dir)+ str(name))