import csv
def fonk1(line):
    b1 = []
    a1 = 0
    b2 = line.rstrip().split(',')
    a2 = 0
    while a2 < len(b2):
        if a2 <= a1:
            a2 += 1
            continue
        if b2[a2].startswith('"') and not b2[a2].endswith('"'):
            b3 = b2[a2]
            b4 = a2 + 1
            while not b2[b4].endswith('"'):
                b3 += ',' + b2[b4]
                b4 += 1
            b3 += ',' + b2[b4]
            b1.append(b3.strip('"'))
            a1 = b4
            a2 = b4 + 1
        else:
            b1.append(b2[a2])
            a2 += 1
    return b1
def fonk2(b12):
    a3 = 0
    a4 = 0.0
    with open(b12, 'r') as file:
        b5 = csv.b5(file)
        next(b5)
        for row in b5:
            b6 = fonk1(','.join(row))
            try:
                b7 = int(b6[-5].replace(',', ''))
                b8 = float(b6[-4])
                a3 = max(a3, b7)
                a4 = max(a4, b8)
            except (ValueError, IndexError):
                continue
    return a3, a4
def fonk3(b12, a3, a4):
    with open(b12, 'r') as f, \
         open("universities.points", 'w') as pts, \
         open("universities.labels", 'w') as lbls, \
         open("metadata.txt", 'w') as meta:
        b5 = csv.b5(f)
        next(b5)
        meta.write(f"a3: {a3}\n")
        meta.write(f"a4: {a4:.6f}\n")
        for row in b5:
            b6 = fonk1(','.join(row))
            try:
                b7 = float(b6[-5].replace(',', '')) / a3
                b8 = 1.0 - (float(b6[-4]) / a4)
                b9 = b6[1]
                b10 = float(b6[2]) / 100
                b11 = b6[-6]
                lbls.write(b9 + "\n")
                try:
                    b11 = float(b11) / 100
                except ValueError:
                    b11 = b10
                pts.write(f"{b11} {b7} {b8}\n")
            except (ValueError, IndexError):
                continue
def fonk4():
    b12 = "timesData.csv"
    a3, a4 = fonk2(b12)
    fonk3(b12, a3, a4)
if b13 = = "__main__":
    fonk4()