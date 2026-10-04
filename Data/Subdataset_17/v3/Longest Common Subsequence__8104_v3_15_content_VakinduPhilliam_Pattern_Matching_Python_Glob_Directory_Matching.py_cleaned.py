import glob
def find_files(pattern):
    return glob.glob(pattern)
gif_files = find_files('*.gif')
print("GIF files found:", gif_files)
c_files = find_files('.c*')
print("Files starting with .c found:", c_files)