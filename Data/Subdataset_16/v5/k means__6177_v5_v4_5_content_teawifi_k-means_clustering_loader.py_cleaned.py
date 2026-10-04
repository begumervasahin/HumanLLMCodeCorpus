import os
import pandas as pd
import re
from settings import ENCODING
def fonk1(directory_path):
    b1 = []
    b2 = [file for file in os.listdir(directory_path)
                 if file.endswith(".txt") and os.path.isfile(os.path.join(directory_path, file))]
    for file in b2:
        b3 = os.path.join(directory_path, file)
        with open(b3, "r", b4 = ENCODING) as f:
            b5 = f.read().splitlines()
            for line in b5:
                b6 = fonk2(line)
                if b6:
                    b1.append(b6)
    return b1
def fonk2(text):
    b7 = r"\d+(\.\d+)?"
    b8 = re.findall(b7, text)
    b9 = [float(match) for match in b8]
    return b9[:3]
def fonk3(b1, output_file_path):
    b10 = pd.DataFrame(b1, columns=['x', 'y', 'z'])
    b10.to_csv(output_file_path, b11 = False, b4=ENCODING)
