from filecmp import dircmp
def fonk1(b4):
    for file_name in b4.diff_files:
        print(f"Different file: {file_name} found in {b4.left} and {b4.right}")
    for subdir_comparison in b4.subdirs.values():
        fonk1(subdir_comparison)
if b1 = = "__main__":
    b2 = 'b2'
    b3 = 'b3'
    b4 = dircmp(b2, b3)
    fonk1(b4)