import re
import pandas as pd
def fonk1(file):
    with open(file, b1 = 'utf-8') as f:
        b2 = []
        b3 = f.read()
        b4 = re.compile(r'\b\d+\s*b7?\b')
        b5 = b4.findall(b3)
        for b6 in b5:
            b6 = re.sub("\D", "", b6)
            b7 = int(b6)
            if b7 <= 10:
                b2.append(b7)
        return b2
def fonk2(file):
    with open(file, b1 = 'utf-8') as f:
        b3 = f.read()
        b8 = len(re.findall(r'diploma', b3, re.IGNORECASE))
        b9 = len(re.findall(r'bachelor.{0,5}degree', b3, re.IGNORECASE))
        b10 = len(re.findall(r'master.{0,5}degree', b3, re.IGNORECASE))
        b11 = len(re.findall(r'phd', b3, re.IGNORECASE))
        print("Number of diploma:", b8)
        print("Number of bachelor's degree:", b9)
        print("Number of master's degree:", b10)
        print("Number of PhD:", b11)
def fonk3(data_list, filename):
    b12 = pd.DataFrame(data={"col1": data_list})
    b12.to_csv(filename, b13 = ',', index=False)
def fonk4():
    b14 = input("Enter the b14 of the JSON file you want to parse: ")
    b15 = fonk1(b14)
    b16 = fonk2(b14)
    fonk3(b15, "b15.csv")
if b17 = = '__main__':
    fonk4()