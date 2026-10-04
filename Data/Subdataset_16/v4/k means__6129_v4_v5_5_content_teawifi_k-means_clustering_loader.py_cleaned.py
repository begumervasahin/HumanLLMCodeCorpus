import os
import pandas as pd
import re
from settings import ENCODING
def fonk1(directory_path):
    b1 = []
    b2 = [file for file in os.listdir(directory_path)
                 if os.path.isfile(os.path.join(directory_path, file)) and file.endswith(".txt")]
    for txt_file in b2:
        b3 = os.path.join(directory_path, txt_file)
        with open(b3, "r", b4 = ENCODING) as file:
            b5 = file.read().split('\n')
            b1.extend(b5)
    b6 = [fonk2(item) for item in b1]
    return b6
def fonk2(b1):
    b7 = r"\d+"
    b8 = re.findall(b7, b1)
    b9 = [float(num_str) for num_str in b8]
    return b9[:3]
def fonk3(b1, csv_file_path):
    b10 = pd.DataFrame(b1, columns=['x', 'y', 'z'])
    b10.to_csv(csv_file_path, b11 = False, b4=ENCODING)
