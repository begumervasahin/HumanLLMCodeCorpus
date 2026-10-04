import os
import pandas as pd
import re
b1 = 'utf-8'
def fonk1(path_to_dir):
    b2 = fonk2(path_to_dir)
    b3 = []
    for file in b2:
        b4 = os.path.join(path_to_dir, file)
        b5 = fonk3(b4)
        b3.extend(b5)
    b6 = [fonk4(line) for line in b3]
    return b6
def fonk2(directory):
    return [
        file for file in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, file)) and file.endswith(".txt")
    ]
def fonk3(b4):
    with open(b4, "r", b7 = b1) as file:
        return file.read().splitlines()
def fonk4(text):
    b8 = r"[0-9]+"
    b9 = re.findall(b8, text)
    b10 = [float(match) for match in b9[:3]]
    return b10
def fonk5(data, b4):
    b11 = pd.DataFrame(data, columns=['x', 'y', 'z'])
    b11.to_csv(b4, b12 = False, b7=b1)
