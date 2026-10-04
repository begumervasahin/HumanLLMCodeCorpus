import os
import re
import pandas as pd
b1 = 'utf-8'
def fonk1(path_to_dir):
    b2 = []
    b3 = [file for file in os.listdir(path_to_dir) if file.endswith(".txt")]
    for file in b3:
        b4 = os.path.join(path_to_dir, file)
        if os.path.isfile(b4):
            with open(b4, "r", b5 = b1) as f:
                b6 = f.read().split('\n')
                b2.extend(b6)
    b7 = [fonk2(item) for item in b2]
    return b7
def fonk2(b2):
    b8 = r"[0-9]+"
    b9 = [float(num) for num in re.findall(b8, b2)]
    return b9[:3]
def fonk3(b2, b4):
    b10 = pd.DataFrame(b2, columns=['x', 'y', 'z'])
    b10.to_csv(b4, b11 = False, b5=b1)
if b12 = = "__main__":
    b13 = "/path/to/directory"
    b14 = "output.csv"
    b2 = fonk1(b13)
    fonk3(b2, b14)