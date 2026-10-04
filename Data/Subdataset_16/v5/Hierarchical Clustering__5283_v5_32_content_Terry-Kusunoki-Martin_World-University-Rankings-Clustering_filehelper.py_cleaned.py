
import csv
def fonk1(line):
    b1 = line.rstrip().split(',')
    b2 = []
    a1 = 0
    while a1 < len(b1):
        if b1[a1].startswith('"') and not b1[a1].endswith('"'):
            b3 = b1[a1]
            b4 = a1 + 1
            while b4 < len(b1) and not b1[b4].endswith('"'):
                b3 += ',' + b1[b4]
                b4 += 1
            b3 += ',' + b1[b4]
            b2.append(b3.strip('"'))
            a1 = b4 + 1
        else:
            b2.append(b1[a1])
            a1 += 1
    return b2
def fonk2(b12):
    a2 = 0
    a3 = 0.0
    with open(b12, 'r') as f:
        b5 = csv.b5(f)
        next(b5)
        for row in b5:
            b6 = fonk1(','.join(row))
            try:
                b7 = int(b6[-5].replace(',', ''))
                b8 = float(b6[-4])
                a2 = max(a2, b7)
                a3 = max(a3, b8)
            except (ValueError, IndexError):
                continue
    return a2, a3
def fonk3(a2, a3):
    with open("metadata.txt", 'w') as meta:
        meta.write(f"a2: {a2}\n")
        meta.write(f"a3: {a3:.6f}\n")
def fonk4(b12, a2, a3):
    with open(b12, 'r') as f, \
         open("universities.points", 'w') as pts, \
         open("universities.labels", 'w') as lbls:
        b5 = csv.b5(f)
        next(b5)
        for row in b5:
            b6 = fonk1(','.join(row))
            try:
                b7 = float(b6[-5].replace(',', '')) / a2
                b8 = 1.0 - (float(b6[-4]) / a3)
                b9 = b6[1]
                b10 = float(b6[2]) / 100
                b11 = b6[-6]
                lbls.write(f"{b9}\n")
                try:
                    b11 = float(b11) / 100
                except ValueError:
                    b11 = b10
                pts.write(f"{b11} {b7} {b8}\n")
            except (ValueError, IndexError):
                continue
def fonk5():
    b12 = "timesData.csv"
    a2, a3 = fonk2(b12)
    fonk3(a2, a3)
    fonk4(b12, a2, a3)
if b13 = = "__main__":
    fonk5()