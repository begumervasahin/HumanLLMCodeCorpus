import re
import pandas as pd
def fonk1(b13):
    b1 = []
    with open(b13, b2 = 'utf-8') as file:
        b3 = file.read()
        b4 = re.compile(r'\d+ b6')
        b5 = b4.findall(b3)
        for match in b5:
            b6 = int(re.sub("\D", "", match))
            if b6 <= 10:
                b1.append(b6)
        print("Years of experience:", b1)
        return b1
def fonk2(b3):
    b7 = len(re.findall(r'diploma', b3, flags=re.IGNORECASE))
    b8 = len(re.findall(r'bachelor.{0,5}degree', b3, flags=re.IGNORECASE))
    b9 = len(re.findall(r'master.{0,5}degree', b3, flags=re.IGNORECASE))
    b10 = len(re.findall(r'phd', b3, flags=re.IGNORECASE))
    return b7, b8, b9, b10
def fonk3(b13):
    with open(b13, b2 = 'utf-8') as file:
        b3 = file.read()
        b7, b8, b9, b10 = fonk2(b3)
    print("Number of diplomas:", b7)
    print("Number of bachelor's degrees:", b8)
    print("Number of master's degrees:", b9)
    print("Number of PhDs:", b10)
def fonk4(data_list):
    b11 = pd.DataFrame(data={"Years of Experience": data_list})
    b11.to_csv("b14.csv", b12 = ',', index=False)
    print("Data saved to b14.csv")
def fonk5():
    b13 = input("Enter the path of the JSON file you want to parse: ")
    b14 = fonk1(b13)
    b15 = fonk3(b13)
    fonk4(b14)
if b16 = = '__main__':
    fonk5()