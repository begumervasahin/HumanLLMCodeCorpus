9. Repository: HarshaliWagh/Data-Mining
   File: Apriori.py
   URL: https:
   Code Content:
def fonk1(freqitem, a3):
    b1 = []
    b2 = []
    for b6 in freqitem.keys():
        b2.append(b6)
    for i in range(0, len(freqitem)- 1, 1):
        for a2 in range(i+1, len(freqitem)):
            b3 = []
            b3.append(b2[i])
            b3.append(b2[a2])
            b1.append(b3)
    b4 = []
    for i in range(len(b1)):
        b5 = []
        b6 = b1[i]
        b7 = ','.join(b6)
        b8 = b7.split(',')
        for b6 in range(0, len(b8)):
            b5.append(b8[b6])
        b4.append(b5)
    b9 = []
    b10 = []
    b11 = []
    for i in range(0, len(b4)):
        b5 = set(b4[i])
        b12 = list(b5)
        b9.append(b12)
        if (len(b9[i]) == a3):
           b10.append(b9[i])
        else:
            b11.append(b9[i])
    return(b10)
def fonk2(can, data):
    b13 = []
    b14 = []
    b15 = []
    for b5 in range(0, len(can)):
        b6 = set(can[b5])
        b16 = set(b6)
        b14.append(b16)
    for b12 in range(0, len(data)):
        b7 = set(data[b12])
        b17 = set(b7)
        b15.append(b17)
    for i in range(0, len(can)):
        a1 = 0
        a2 = 0
        for a2 in range(0, len(data)):
            if((b14[i]).issubset(b15[a2])):
                a1 = a1 + 1
            a2 = a2 + 1
        b13.append(a1)
    return(b13)
def fonk3(b36, b37, b30):
    b18 = {}
    for i in range(0, len(b36)):
        b6 = b36[i]
        b7 = ','.join(b6)
        if(b37[i] >= b30):
            b18[b7] = b37[i]
    return(b18)
def fonk4(b38, a3):
    b15 = a3 - 1
    b19 = []
    for x in b38:
        b6 = x.split(',')
        b19.append(b6)
    while(b15 !=0):
        for i in range(0, len(b19)):
            b20 = []
            b21 = fonk5(b19[i], b20, b15)
            print(b21)
            for a2 in range(0, len(b21)):
                b22 = []
                for k in range(0, len(b19[i])):
                    if (b19[a2][k] not in b21[a2]):
                        b22.append(b19[i][k])
                        print(str(b22)+"--------->"+str(b21[a2]))
        b15 = b15 - 1
    '''b23 = []
    b24 = []
    b25 = []
    for trans in b28:
        if set(b22[0]).issubset(set(trans)):
            b24 = b24 + 1
        if set(b22[0] + b22[i]).issubset(set(trans)):
            b25 - b25 + 1
        b26 = (b25 / b24) * 100
        if b26 >= b31:
            print(b26)'''
def fonk5(b18, b20, b15):
    if len(b18) == b15:
        if b20.a3(b18) == 0:
            b20.append(b18)
        return b20
    elif len(b18)!= b15:
        for i in range(0,len(b18)):
            b27 = b18[i+1:] + b18[:i]
            b20 = fonk5(b27, b20, b15)
        return b20
b28 = []
print("Select the b28:")
print("1 grocery")
print("2 clothing")
print("3 electronics")
print("4 utensils")
print("5 furniture")
b29 = input("Enter number ")
b30 = int(input('Enter minimum Support: '))
b31 = int(input('Enter minimum Confidence: '))
b32 = ""
if b29 = = '1':
    b32 = "db1.txt"
elif b29 = = '2':
    b32 = "db2.txt"
elif b29 = = '3':
    b32 = "db3.txt"
elif b29 = = '4':
    b32 = "db4.txt"
else:
    b32 = "db5.txt"
b33 = open(b32, 'r')
while True:
    b34 = b33.readline()
    if not b34 :
        break;
    b34 = b34.rstrip()
    b28.append(b34.split(", "))
b35 = {}
for data in b28:
    for b2 in data:
        if b2 in b35:
            b35[b2] = b35[b2] + 1
        else:
            b35[b2] = 1
b18 = {}
for i in range(0, len(b35)):
    for b2, a3 in b35.items():
        if(a3 >= b30):
            b18[b2] = a3
a3 = 2
b36 = fonk1(b18, a3)
b37 = fonk2(b36, b28)
b38 = fonk3(b36, b37, b30)
b39 = fonk4(b38, a3)
a4 = 0
a3 = 3
while(a4 = = 0):
    b36 = fonk1(b38, a3)
    b37 = fonk2(b36, b28)
    b38 = fonk3(b36, b37, b30)
    b39 = fonk4(b38, a3)
    a3 = a3 + 1
    for i in range(0, len(b37)):
        if(b37[i] >= b30):
            a4 = 0
            break
        else:
            a4 = 1
            break
   README Content:
This code attempts to implements Apriori algorithm in Python from scratch.
List of Files -
1. Apriori.py
2 Dataset files - db1.txt, db2.txt, db3.txt, db4.txt, db5.txt
3 README file(this file)
