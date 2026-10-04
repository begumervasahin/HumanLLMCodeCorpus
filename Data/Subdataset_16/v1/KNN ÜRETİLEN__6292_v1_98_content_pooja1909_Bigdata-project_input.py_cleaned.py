import csv
from collections import defaultdict
def fonk1(b6):
    with open('output.csv', 'w', b1 = '') as clusterfile:
        b2 = csv.b2(clusterfile)
        b3 = defaultdict(list)
        with open(b6, 'r') as f:
            b4 = csv.b4(f)
            b5 = next(b4)
            b2.writerow([b5[12], b5[13], b5[9]])
            f.seek(0)
            b4 = csv.DictReader(f)
            for row in b4:
                for (k, v) in row.items():
                    b3[k].append(v)
            for i in range(len(b3["Lon"])):
                b2.writerow([b3["Lon"][i], b3["Lat"][i], b3["Text_General_Code"][i]])
def fonk2():
    b6 = 'input.csv'
    fonk1(b6)
if b7 = = "__main__":
    fonk2()