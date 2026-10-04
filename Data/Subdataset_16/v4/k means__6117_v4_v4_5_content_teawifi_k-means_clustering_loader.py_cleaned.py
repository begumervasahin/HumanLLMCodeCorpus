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
            b4 = f.read().splitlines()
            for line in b4:
                b5 = fonk2(line)
                if b5:
                    b1.append(b5)
    return b1
def fonk2(b1):
    b6 = r"\d+(\.\d+)?"
    b7 = re.findall(b6, b1)
    b8 = [float(num) for num in b7]
    return b8[:3]
def fonk3(b1, file_path):
    b9 = pd.DataFrame(b1, columns=['x', 'y', 'z'])
    b9.to_csv(file_path, b10 = False, b3=ENCODING)
