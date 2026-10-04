import glob
def fonk1():
    b1 = glob.glob('./[0-9].*')
    print("Files starting with a digit followed by any character(s):", b1)
    b2 = glob.glob('*.gif')
    print("All .gif files in the current directory:", b2)
    b3 = glob.glob('?.gif')
    print("Single-character .gif files in the current directory:", b3)
    b4 = glob.glob('**/*.txt', recursive=True)
    print("All .txt files in the current directory and subdirectories:", b4)
    b5 = glob.glob('./**/', recursive=True)
    print("All directories in the current directory and subdirectories:", b5)
if b6 = = "__main__":
    fonk1()