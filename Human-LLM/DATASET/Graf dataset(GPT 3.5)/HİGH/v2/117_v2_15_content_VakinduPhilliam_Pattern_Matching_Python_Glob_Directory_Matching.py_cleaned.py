
import glob
b1 = glob.glob('*.gif')
print("Here are the GIF files I found in this folder:")
print(b1)
b2 = glob.glob('.c*')
print("\nAnd here are the files that start with 'c':")
print(b2)