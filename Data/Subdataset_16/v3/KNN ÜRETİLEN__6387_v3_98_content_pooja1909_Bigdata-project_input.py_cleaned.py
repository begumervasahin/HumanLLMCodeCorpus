import csv
from collections import defaultdict
def fonk1(b9, b1 = 'output.csv'):
    b2 = defaultdict(list)
    with open(b9, 'r') as infile:
        b3 = csv.b3(infile)
        b4 = next(b3)
        infile.seek(0)
        b5 = csv.DictReader(infile)
        for row in b5:
            for key, value in row.items():
                b2[key].append(value)
    b6 = ['Lon', 'Lat', 'Text_General_Code']
    with open(b1, 'w', b7 = '') as outfile:
        b8 = csv.b8(outfile)
        b8.writerow(b6)
        for i in range(len(b2['Lon'])):
            b8.writerow([b2['Lon'][i], b2['Lat'][i], b2['Text_General_Code'][i]])
def fonk2():
    b9 = 'input.csv'
    fonk1(b9)
if b10 = = "__main__":
    fonk2()