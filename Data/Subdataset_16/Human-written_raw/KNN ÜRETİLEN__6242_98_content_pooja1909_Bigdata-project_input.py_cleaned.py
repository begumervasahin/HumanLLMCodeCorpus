import csv
from collections import defaultdict
def fonk1(b6):
    b1 = open('output.csv', 'w')
    b2 = defaultdict(list)
    b3 = open("input.csv", "rb")
    b4 = csv.b4(b3)
    b5 = b4.next()
    b1.write(b5[12])
    b1.write(",")
    b1.write(b5[13])
    b1.write(",")
    b1.write(b5[9])
    b1.write("\n")
    with open("input.csv", "rb") as fp:
        b4 = csv.DictReader(fp)
        for row in b4:
            for (k,v) in row.items():
                b2[k].append(v)
        for i in range(len(b2["Lon"])):
            b1.write(b2["Lon"][i])
            b1.write(",")
            b1.write(b2["Lat"][i])
            b1.write(",")
            b1.write(b2["Text_General_Code"][i])
            b1.write("\n")
def fonk2():
    b6 = 'input.csv'
    fonk1(b6)
fonk2()