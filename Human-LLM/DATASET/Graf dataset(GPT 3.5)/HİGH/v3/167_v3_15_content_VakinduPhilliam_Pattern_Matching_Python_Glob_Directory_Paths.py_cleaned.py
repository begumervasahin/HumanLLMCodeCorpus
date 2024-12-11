import glob
def fonk1(pattern, description):
    b1 = glob.glob(pattern)
    print(f"{description}:", b1)
def fonk2():
    b2 = './[0-9].*'
    fonk1(b2, "Files starting with a digit in the current directory")
    b3 = '*.gif'
    fonk1(b3, "GIF files in the current directory")
    b4 = '?.gif'
    fonk1(b4, "Single character named GIF files in the current directory")
    b5 = '**/*.txt'
    fonk1(b5, "Text files in the current directory and subdirectories", True)
    b6 = './**/'
    fonk1(b6, "Directories in the current directory and subdirectories", True)
if b7 = = '__main__':
    fonk2()