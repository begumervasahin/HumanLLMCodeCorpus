import os
import pandas as pd
import re
from settings import ENCODING
def fonk1(directory_path):
    b1 = []
    b2 = fonk2(directory_path)
    for txt_file in b2:
        b3 = os.path.join(directory_path, txt_file)
        b4 = fonk3(b3)
        b1.extend(b4)
    b5 = [fonk4(item) for item in b1]
    return b5
def fonk2(directory_path):
    return [file for file in os.listdir(directory_path)
            if os.path.isfile(os.path.join(directory_path, file)) and file.endswith(".txt")]
def fonk3(b3):
    with open(b3, "r", b6 = ENCODING) as file:
        return file.read().split('\n')
def fonk4(b1):
    b7 = r"\d+"
    b8 = re.findall(b7, b1)
    b9 = [float(num_str) for num_str in b8]
    return b9[:3]
def fonk5(b1, csv_file_path):
    b10 = pd.DataFrame(b1, columns=['x', 'y', 'z'])
    b10.to_csv(csv_file_path, b11 = False, b6=ENCODING)
