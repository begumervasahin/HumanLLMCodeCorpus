__author__ = 'huaijun'
import os
from os import path
def load_txt(file):
    with open(file,'r') as f_h:
        res = f_h.read()
        return res
rootdir = os.getcwd()
dirs = os.listdir(rootdir)
filedirs = [ele for ele in dirs if ele.startswith('C0')]
samplefile = path.join(rootdir, 'sample')
if not path.isdir(samplefile):
    os.mkdir(samplefile)
with open(path.join(rootdir,'wrong_code.txt'),'a+') as log_f:
    for dir in filedirs:
        donedir = path.join(samplefile,dir)
        if not path.isdir(donedir):
            os.mkdir(donedir)
        fileurl = path.join(rootdir,dir)
        sondirs = os.listdir(fileurl)
        for name in sondirs:
            try:
                text = load_txt(path.join(fileurl,name))
                with open(path.join(donedir,name),'w',encoding = 'utf-8') as w_f:
                    w_f.write(text)
            except (IOError, UnicodeDecodeError, FileNotFoundError):
                log_f.write('éè¯¯çç¼ç '+str(dir)+ str(name))