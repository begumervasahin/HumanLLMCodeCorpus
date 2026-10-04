from filecmp import dircmp
def fonk1(b1):
    for name in b1.diff_files:
        print(f"Different file {name} found in {b1.left} and {b1.right}")
    for sub_dcmp in b1.subdirs.values():
        fonk1(sub_dcmp)
b1 = dircmp('dir1', 'dir2')
fonk1(b1)