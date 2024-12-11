import re
import pandas as pd
def fonk1(b10):
    with open(b10, b1 = 'utf-8') as file:
        b2 = file.read()
        b3 = [int(year.strip(" years")) for year in re.findall(r'\b\d+\s*years?\b', b2) if int(year.strip(" years")) <= 10]
        return b3
def fonk2(b10):
    with open(b10, b1 = 'utf-8') as file:
        b2 = file.read()
        b4 = len(re.findall(r'diploma', b2, re.IGNORECASE))
        b5 = len(re.findall(r'bachelor.{0,5}degree', b2, re.IGNORECASE))
        b6 = len(re.findall(r'master.{0,5}degree', b2, re.IGNORECASE))
        b7 = len(re.findall(r'phd', b2, re.IGNORECASE))
        print("Number of diploma:", b4)
        print("Number of bachelor's degree:", b5)
        print("Number of master's degree:", b6)
        print("Number of PhD:", b7)
def fonk3(data_list, filename):
    b8 = pd.DataFrame(data={"Experience Years": data_list})
    b8.to_csv(filename, b9 = ',', index=False)
def fonk4():
    b10 = input("Enter the path of the JSON file you want to parse: ")
    b11 = fonk1(b10)
    fonk2(b10)
    fonk3(b11, "b11.csv")
if b12 = = '__main__':
    fonk4()