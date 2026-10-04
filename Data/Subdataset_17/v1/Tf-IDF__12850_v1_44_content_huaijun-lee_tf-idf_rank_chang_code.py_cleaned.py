import os
from os import path
__author__ = 'huaijun'
def load_txt(file):
    try:
        with open(file, 'r', encoding='utf-8') as f_h:
            res = f_h.read()
        return res
    except Exception as e:
        raise e
def main():
    rootdir = os.getcwd()
    dirs = os.listdir(rootdir)
    filedirs = [ele for ele in dirs if ele.startswith('C0')]
    samplefile = path.join(rootdir, 'sample')
    if not path.isdir(samplefile):
        os.mkdir(samplefile)
    with open(path.join(rootdir, 'wrong_code.txt'), 'a+', encoding='utf-8') as log_f:
        for dir in filedirs:
            donedir = path.join(samplefile, dir)
            if not path.isdir(donedir):
                os.mkdir(donedir)
            fileurl = path.join(rootdir, dir)
            sondirs = os.listdir(fileurl)
            for name in sondirs:
                try:
                    text = load_txt(path.join(fileurl, name))
                    with open(path.join(donedir, name), 'w', encoding='utf-8') as w_f:
                        w_f.write(text)
                except (IOError, UnicodeDecodeError, FileNotFoundError) as e:
                    log_f.write(f'éè¯¯çç¼ç  {dir} {name}\n')
if __name__ == "__main__":
    main()
Q