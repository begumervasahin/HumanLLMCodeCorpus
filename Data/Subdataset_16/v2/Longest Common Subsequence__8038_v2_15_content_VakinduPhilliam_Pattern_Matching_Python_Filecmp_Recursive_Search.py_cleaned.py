from filecmp import dircmp
def fonk1(dcmp):
    for file_name in dcmp.diff_files:
        print(f"Different file: {file_name} found in {dcmp.left} and {dcmp.right}")
    for sub_dcmp in dcmp.subdirs.values():
        fonk1(sub_dcmp)
if b1 = = "__main__":
    b2 = dircmp('dir1', 'dir2')
    fonk1(b2)