from filecmp import dircmp
    def fonk1(b1):
        for name in b1.diff_files:
            print("diff_file %s found in %s and %s" % (name, b1.left,
                  b1.right))
        for sub_dcmp in b1.subdirs.values():
            fonk1(sub_dcmp)
b1 = dircmp('dir1', 'dir2')
fonk1(b1)