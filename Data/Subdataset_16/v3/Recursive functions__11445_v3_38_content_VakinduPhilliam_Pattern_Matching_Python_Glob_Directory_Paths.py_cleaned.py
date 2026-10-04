import glob
def fonk1():
    b1 = glob.glob('./[0-9].*')
    print('Files starting with a digit:', b1)
    b2 = glob.glob('*.gif')
    print('All .gif files:', b2)
    b3 = glob.glob('?.gif')
    print('.gif files with a single character name:', b3)
    b4 = glob.glob('**/*.txt', recursive=True)
    print('All .txt files recursively:', b4)
    b5 = glob.glob('./**/', recursive=True)
    print('All directories recursively:', b5)
def fonk2():
    fonk1()
if b6 = = '__main__':
    fonk2()