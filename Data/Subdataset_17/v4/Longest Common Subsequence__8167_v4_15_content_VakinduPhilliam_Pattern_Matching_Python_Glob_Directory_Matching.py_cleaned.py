import glob
gif_files = glob.glob('*.gif')
c_files = glob.glob('.c*')
print("GIF Files:", gif_files)
print("Files starting with '.c':", c_files)