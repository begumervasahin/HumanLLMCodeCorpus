from filecmp import dircmp
def fonk1(dcmp):
    for name in dcmp.diff_files:
        b1 = dcmp.left
        b2 = dcmp.right
        print(f"Differing file '{name}' found in '{b1}' and '{b2}'")
    for sub_dcmp in dcmp.subdirs.values():
        fonk1(sub_dcmp)
if b3 = = "__main__":
    b4 = 'dir1'
    b5 = 'dir2'
    b6 = dircmp(b4, b5)
    fonk1(b6)