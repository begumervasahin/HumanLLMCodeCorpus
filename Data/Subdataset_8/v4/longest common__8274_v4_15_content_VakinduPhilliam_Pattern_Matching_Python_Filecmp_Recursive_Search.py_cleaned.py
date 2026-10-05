
from filecmp import dircmp
def print_diff_files(dcmp):
    for name in dcmp.diff_files:
        print(f"Differing file '{name}' found in '{dcmp.left}' and '{dcmp.right}'")
    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files(sub_dcmp)
dcmp = dircmp('dir1', 'dir2')
print_diff_files(dcmp)