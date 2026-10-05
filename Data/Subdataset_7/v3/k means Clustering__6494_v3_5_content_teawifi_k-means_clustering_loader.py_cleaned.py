import os
import re
import pandas as pd
b1 = 'utf-8'
def fonk1(path_to_dir):
    b2 = []
    b3 = [file for file in os.listdir(path_to_dir)
             if os.path.isfile(os.path.join(path_to_dir, file)) and file.endswith(".txt")]
    for file in b3:
        with open(os.path.join(path_to_dir, file), "r", b4 = b1) as f:
            b5 = f.read().split('\n')
            b2.extend(b5)
    b6 = [fonk2(item) for item in b2]
    return b6
def fonk2(b2):
    b7 = "[0-9]+"
    b8 = re.findall(b7, b2)
    b9 = [float(i) for i in b8]
    return b9[:3]
def fonk3(b2, file_path):
    b10 = pd.DataFrame(b2, columns=['x', 'y', 'z'])
    b10.to_csv(file_path, b11 = False, b4=b1)
if b12 = = "__main__":
    b13 = "/path/to/directory"
    b14 = "output.csv"
    b2 = fonk1(b13)
    fonk3(b2, b14)