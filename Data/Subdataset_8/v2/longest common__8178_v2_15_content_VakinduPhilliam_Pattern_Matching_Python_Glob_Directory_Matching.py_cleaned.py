
import glob
gif_files = glob.glob('*.gif')
print("Here are the GIF files I found in this folder:")
print(gif_files)
c_files = glob.glob('.c*')
print("\nAnd here are the files that start with 'c':")
print(c_files)