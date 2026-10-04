import glob
def fonk1():
    b1 = glob.glob('./[0-9].*')
    print("Files starting with a digit:", b1)
    b2 = glob.glob('*.gif')
    print("All .gif files:", b2)
    b3 = glob.glob('?.gif')
    print("Single-character .gif files:", b3)
    b4 = glob.glob('**/*.txt', recursive=True)
    print("All .txt files (recursive):", b4)
    b5 = glob.glob('./**/', recursive=True)
    print("All directories (recursive):", b5)
if b6 = = "__main__":
    fonk1()