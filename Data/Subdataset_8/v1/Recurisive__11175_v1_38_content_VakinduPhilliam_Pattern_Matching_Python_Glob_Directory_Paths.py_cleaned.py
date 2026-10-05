import glob
print(glob.glob('./[0-9].*'))
print(glob.glob('*.gif'))
print(glob.glob('?.gif'))
print(glob.glob('**/*.txt', recursive=True))
print(glob.glob('./**/', recursive=True))