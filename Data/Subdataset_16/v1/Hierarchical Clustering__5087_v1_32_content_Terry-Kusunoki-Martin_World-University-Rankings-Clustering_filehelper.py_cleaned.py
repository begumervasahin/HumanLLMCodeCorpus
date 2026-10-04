def fonk1(line):
    b1 = []
    a1 = 0
    b2 = line.rstrip().split(',')
    for i in range(len(b2)):
        if i <= a1:
            continue
        if '"' in b2[i]:
            b3 = b2[i]
            b4 = i + 1
            while '"' not in b2[b4]:
                b3 += ',' + b2[b4]
                b4 += 1
            b3 += ',' + b2[b4]
            b1.append(b3.strip('"'))
            a1 = b4
        else:
            b1.append(b2[i])
    return b1
def fonk2(b11):
    a2 = 0
    a3 = 0.0
    with open(b11, 'r') as file:
        for line in file:
            b5 = fonk1(line)
            if b5[0] == "world_rank":
                continue
            try:
                b6 = int(b5[-5].replace(',', ''))
                b7 = float(b5[-4])
                a2 = max(a2, b6)
                a3 = max(a3, b7)
            except (ValueError, IndexError):
                continue
    return a2, a3
def fonk3(b11, a2, a3):
    with open(b11, 'r') as f, \
         open("universities.points", 'w') as pts, \
         open("universities.labels", 'w') as lbls, \
         open("metadata.txt", 'w') as meta:
        meta.write(f"a2: {a2}\n")
        meta.write(f"a3: {a3:.6f}\n")
        for line in f:
            b5 = fonk1(line)
            if b5[0] == "world_rank":
                continue
            try:
                b6 = float(b5[-5].replace(',', '')) / a2
                b7 = 1.0 - (float(b5[-4]) / a3)
                b8 = b5[1]
                b9 = float(b5[2]) / 100
                b10 = b5[-6]
                lbls.write(b8 + "\n")
                try:
                    b10 = float(b10) / 100
                except ValueError:
                    b10 = b9
                pts.write(f"{b10} {b6} {b7}\n")
            except (ValueError, IndexError):
                continue
def fonk4():
    b11 = "timesData.csv"
    a2, a3 = fonk2(b11)
    fonk3(b11, a2, a3)
if b12 = = "__main__":
    fonk4()