import os
import re
import pandas as pd
b1 = 'utf-8'
def fonk1(directory_path):
    b2 = []
    b3 = [file for file in os.listdir(directory_path) if file.endswith(".txt")]
    for txt_file in b3:
        b4 = os.path.join(directory_path, txt_file)
        with open(b4, "r", b5 = b1) as file:
            b6 = file.readlines()
            b2.extend(b6)
    b7 = [fonk2(line) for line in b2]
    return b7
def fonk2(text):
    b8 = r"[0-9]+"
    b9 = re.findall(b8, text)
    b10 = [float(num) for num in b9]
    return b10[:3]
def fonk3(b2, output_path):
    b11 = pd.DataFrame(b2, columns=['x', 'y', 'z'])
    b11.to_csv(output_path, b12 = False, b5=b1)
def fonk4():
    b13 = "/path/to/directory"
    b14 = "output.csv"
    b7 = fonk1(b13)
    fonk3(b7, b14)
if b15 = = "__main__":
    fonk4()