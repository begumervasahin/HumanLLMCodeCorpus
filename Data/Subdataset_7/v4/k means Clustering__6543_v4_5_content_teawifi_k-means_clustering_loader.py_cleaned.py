import os
import pandas as pd
import re
from settings import ENCODING
def fonk1(path_to_dir):
    b1 = []
    b2 = [file for file in os.listdir(path_to_dir)
             if os.path.isfile(os.path.join(path_to_dir, file)) and file.endswith(".txt")]
    for file in b2:
        with open(os.path.join(path_to_dir, file), "r", b3 = ENCODING) as f:
            b4 = f.read().split('\n')
            b1.extend(b4)
    b5 = []
    for item in b1:
        b5.append(fonk2(item))
    return b5
def fonk2(b1):
    b6 = "[0-9]+"
    b7 = re.findall(b6, b1)
    b8 = [float(i) for i in b7]
    return b8[:3]
def fonk3(b1, file_path):
    b9 = pd.DataFrame(b1)
    b9.to_csv(file_path, b10 = False, b3=ENCODING, header=['x', 'y', 'z'])
