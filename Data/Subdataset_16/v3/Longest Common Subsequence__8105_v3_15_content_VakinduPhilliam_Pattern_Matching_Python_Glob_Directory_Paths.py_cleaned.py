import glob
def fonk1(pattern, description):
    b1 = glob.glob(pattern, recursive=True)
    print(f"{description}: {b1}")
def fonk2():
    fonk1('./[0-9].*', "Files starting with a digit followed by any character(s)")
    fonk1('*.gif', "All .gif files in the current directory")
    fonk1('?.gif', "Single-character .gif files in the current directory")
    fonk1('**/*.txt', "All .txt files in the current directory and subdirectories")
    fonk1('./**/', "All directories in the current directory and subdirectories")
if b2 = = "__main__":
    fonk2()