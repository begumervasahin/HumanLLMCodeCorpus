import csv
from collections import defaultdict
def fonk1(b7):
    b1 = 'output.csv'
    with open(b1, 'w', b2 = '') as clusterfile:
        b3 = csv.b3(clusterfile)
        with open(b7, 'r', b2 = '') as f:
            b4 = csv.b4(f)
            b5 = next(b4)
            b3.writerow([b5[12], b5[13], b5[9]])
            b6 = defaultdict(list)
            b4 = csv.DictReader(f, fieldnames=b5)
            for row in b4:
                for k, v in row.items():
                    b6[k].append(v)
            for i in range(len(b6["Lon"])):
                b3.writerow([b6["Lon"][i], b6["Lat"][i], b6["Text_General_Code"][i]])
def fonk2():
    b7 = 'input.csv'
    fonk1(b7)
if b8 = = "__main__":
    fonk2()