import os
import pandas as pd
import re
from settings import ENCODING
def fonk1(directory_path):
    b1 = []
    b2 = [file for file in os.listdir(directory_path)
                 if os.path.isfile(os.path.join(directory_path, file)) and file.endswith(".txt")]
    for txt_file in b2:
        with open(os.path.join(directory_path, txt_file), "r", b3 = ENCODING) as file:
            b4 = file.read().split('\n')
            b1.extend(b4)
    b5 = [fonk2(item) for item in b1]
    return b5
def fonk2(b1):
    b6 = "[0-9]+"
    b7 = re.findall(b6, b1)
    b8 = [float(num_str) for num_str in b7]
    return b8[:3]
def fonk3(b1, csv_file_path):
    b9 = pd.DataFrame(b1, columns=['x', 'y', 'z'])
    b9.to_csv(csv_file_path, b10 = False, b3=ENCODING)
