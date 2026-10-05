import glob
b1 = glob.glob('./[0-9].*')
b2 = glob.glob('*.gif')
b3 = glob.glob('?.gif')
b4 = glob.glob('**/*.txt', recursive=True)
b5 = glob.glob('./**/', recursive=True)