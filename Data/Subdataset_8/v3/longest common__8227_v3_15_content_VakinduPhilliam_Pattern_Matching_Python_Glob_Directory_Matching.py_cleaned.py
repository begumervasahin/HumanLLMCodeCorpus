import glob
gif_files = glob.glob('*.gif')
print("GIF files found in this folder:")
print(gif_files)
c_files = glob.glob('.c*')
print("\nFiles starting with 'c' found in this folder:")
print(c_files)