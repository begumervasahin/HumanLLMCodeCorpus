import os
import pandas as pd
import re
b1 = 'utf-8'
def fonk1(directory_path):
    b2 = []
    b3 = [file for file in os.listdir(directory_path)
                 if os.path.isfile(os.path.join(directory_path, file)) and file.endswith(".txt")]
    for txt_file in b3:
        b4 = os.path.join(directory_path, txt_file)
        b2.extend(fonk2(b4))
    b5 = [fonk3(item) for item in b2]
    return b5
def fonk2(b4):
    with open(b4, "r", b6 = b1) as file:
        return file.read().split('\n')
def fonk3(b2):
    b7 = r"[0-9]+"
    b8 = re.findall(b7, b2)
    b9 = [float(num_str) for num_str in b8]
    return b9[:3]
def fonk4(b2, csv_file_path):
    b10 = pd.DataFrame(b2, columns=['x', 'y', 'z'])
    b10.to_csv(csv_file_path, b11 = False, b6=b1)
