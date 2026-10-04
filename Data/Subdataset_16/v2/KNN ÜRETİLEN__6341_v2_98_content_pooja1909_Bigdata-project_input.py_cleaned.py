import csv
from collections import defaultdict
def fonk1(b8, b1 = 'output.csv'):
    b2 = defaultdict(list)
    with open(b8, 'r') as infile:
        b3 = csv.b3(infile)
        b4 = next(b3)
        infile.seek(0)
        b5 = csv.DictReader(infile)
        for row in b5:
            for (k, v) in row.items():
                b2[k].append(v)
    with open(b1, 'w', b6 = '') as outfile:
        b7 = csv.b7(outfile)
        b7.writerow([b4[12], b4[13], b4[9]])
        for i in range(len(b2["Lon"])):
            b7.writerow([b2["Lon"][i], b2["Lat"][i], b2["Text_General_Code"][i]])
def fonk2():
    b8 = 'input.csv'
    fonk1(b8)
if b9 = = "__main__":
    fonk2()