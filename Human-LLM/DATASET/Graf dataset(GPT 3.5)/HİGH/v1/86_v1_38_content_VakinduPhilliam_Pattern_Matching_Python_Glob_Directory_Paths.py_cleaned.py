import glob
print(glob.glob('./[0-9].*'))
print(glob.glob('*.gif'))
print(glob.glob('?.gif'))
print(glob.glob('**/*.txt', b1 = True))
print(glob.glob('./**/', b1 = True))