import os
from filecmp import dircmp
def fonk1(b3):
    for name in b3.diff_files:
        print(f"Differing file {name} found in {b3.left} and {b3.right}")
    for sub_dcmp in b3.subdirs.values():
        fonk1(sub_dcmp)
def fonk2():
    b1 = 'b1'
    b2 = 'b2'
    if not (os.path.exists(b1) and os.path.exists(b2)):
        print("Error: One or both directories do not exist.")
        return
    b3 = dircmp(b1, b2)
    fonk1(b3)
if b4 = = "__main__":
    fonk2()