import csv
from collections import defaultdict
def fonk1(b8, b1 = 'output.csv'):
    with open(b1, 'w', b2 = '') as clusterfile:
        b3 = csv.b3(clusterfile)
        with open(b8, 'r', b2 = '') as f:
            b4 = csv.b4(f)
            b5 = next(b4)
            b6 = ["Lon", "Lat", "Text_General_Code"]
            b3.writerow([b5[12], b5[13], b5[9]])
            b7 = defaultdict(list)
            b4 = csv.DictReader(f, fieldnames=b5)
            for row in b4:
                for k, v in row.items():
                    b7[k].append(v)
            for i in range(len(b7["Lon"])):
                b3.writerow([b7["Lon"][i], b7["Lat"][i], b7["Text_General_Code"][i]])
def fonk2():
    b8 = 'input.csv'
    fonk1(b8)
if b9 = = "__main__":
    fonk2()