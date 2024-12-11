import re
import pandas as pd
def fonk1(b9):
    b1 = []
    with open(b9, b2 = 'utf-8') as file:
        b3 = file.read()
        b4 = re.compile(r'\d+ b6')
        b5 = b4.findall(b3)
        for match in b5:
            b6 = int(re.sub("\D", "", match))
            if b6 <= 10:
                b1.append(b6)
        print("Years of experience:", b1)
        return b1
def fonk2(b9):
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    with open(b9, b2 = 'utf-8') as file:
        b3 = file.read()
        a1 = len(re.findall(r'diploma', b3, flags=re.IGNORECASE))
        a2 = len(re.findall(r'bachelor.{0,5}degree', b3, flags=re.IGNORECASE))
        a3 = len(re.findall(r'master.{0,5}degree', b3, flags=re.IGNORECASE))
        a4 = len(re.findall(r'phd', b3, flags=re.IGNORECASE))
    print("Number of diplomas:", a1)
    print("Number of bachelor's degrees:", a2)
    print("Number of master's degrees:", a3)
    print("Number of PhDs:", a4)
def fonk3(data_list):
    b7 = pd.DataFrame(data={"col1": data_list})
    b7.to_csv("experience_years.csv", b8 = ',', index=False)
    print("Data saved to experience_years.csv")
def fonk4():
    b9 = input("Enter the path of the JSON file you want to parse: ")
    fonk1(b9)
    fonk2(b9)
if b10 = = '__main__':
    fonk4()