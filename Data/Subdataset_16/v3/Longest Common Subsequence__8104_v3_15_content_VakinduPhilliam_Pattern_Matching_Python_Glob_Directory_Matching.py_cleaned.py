import glob
def fonk1(pattern):
    return glob.glob(pattern)
b1 = fonk1('*.gif')
print("GIF files found:", b1)
b2 = fonk1('.c*')
print("Files starting with .c found:", b2)