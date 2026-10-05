import os
from filecmp import dircmp
def print_diff_files(dcmp):
    for name in dcmp.diff_files:
        print(f"Differing file '{name}' found in '{dcmp.left}' and '{dcmp.right}'")
    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files(sub_dcmp)
def main():
    dir1 = 'dir1'
    dir2 = 'dir2'
    if not (os.path.exists(dir1) and os.path.exists(dir2)):
        print("Error: One or both directories do not exist.")
        return
    dcmp = dircmp(dir1, dir2)
    print_diff_files(dcmp)
if __name__ == "__main__":
    main()