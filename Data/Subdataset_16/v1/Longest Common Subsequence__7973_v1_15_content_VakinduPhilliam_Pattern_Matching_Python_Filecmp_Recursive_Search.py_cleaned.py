from filecmp import dircmp
def fonk1(b2):
    for name in b2.diff_files:
        print("diff_file %s found in %s and %s" % (name, b2.left, b2.right))
    for sub_dcmp in b2.subdirs.values():
        fonk1(sub_dcmp)
if b1 = = "__main__":
    b2 = dircmp('dir1', 'dir2')
    fonk1(b2)