import re
import pandas
b1 = r"enter the b1 of the json file you want to parse"
def fonk1(file):
    with open(file, b2 = 'utf-8') as f:
        b3 = []
        b4 = f.read()
        b5 = re.compile(r'.{8}years')
        b6 = b5.findall(b4)
        for b7 in b6:
            b7 = re.sub("\D","",str(b7))
            b3.append(str(b7))
        while '' in b3:
            b3.remove('')
        b3 = list(map(int, b3))
        b3 = [year for year in b3 if year <= 10]
        print(b3)
        return  b3
def fonk2(file):
    with open(file, b2 = 'utf-8') as f:
        b8 = []
        b9 = []
        b10 = []
        b11 = []
        b4 = f.read()
        b12 = re.compile(r'b8', flags=re.IGNORECASE)
        b13 = b12.findall(b4)
        for b7 in b13:
            b8.append(b7)
        print("number of b8: " + str(len(b8)))
        b14 = re.compile(r'bachelor.{0,5}degree', flags=re.IGNORECASE)
        b15 = b14.findall(b4)
        for b7 in b15:
            b9.append(b7)
        print("number of bachelor's degree: " + str(len(b9)))
        b5 = re.compile(r'master.{0,5}degree',flags=re.IGNORECASE)
        b6 = b5.findall(b4)
        for b7 in b6:
            b10.append(b7)
        print("number of master's degree: "+str(len(b10)))
        b16 = re.compile(r'phd', flags=re.IGNORECASE)
        b17 = b16.findall(b4)
        for b7 in b17:
            b11.append(b7)
        print("number of b11: " + str(len(b11)))
def fonk3(list):
    b18 = pandas.DataFrame(data={"col1": list})
    b18.to_csv("experience_years.csv", b19 = ',', index=False)
def fonk4():
    fonk2(b1)
if b20 = = '__main__':
    fonk4()