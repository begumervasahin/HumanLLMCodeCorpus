import glob
b1 = glob.glob('*.gif')
print("GIF files found in this folder:")
print(b1)
b2 = glob.glob('.c*')
print("\nFiles starting with 'c' found in this folder:")
print(b2)