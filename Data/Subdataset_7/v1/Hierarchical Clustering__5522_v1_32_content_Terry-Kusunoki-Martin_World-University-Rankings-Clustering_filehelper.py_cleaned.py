def fonk1():
    with open("timesData.csv", 'r') as f, open("universities.points", 'w') as pts, \
         open("universities.labels", 'w') as lbls, open("metadata.txt", 'w') as meta:
        a1 = 0
        a2 = 0
        a3 = 0.0
        for line in f.readlines():
            b1 = line.rstrip().split(',')
            if b1[0] == "world_rank":
                continue
            else:
                b2 = []
                a4 = 0
                for i in range(len(b1)):
                    if i <= a4:
                        continue
                    if '"' in b1[i]:
                        b3 = b1[i]
                        b4 = i + 1
                        while '"' not in b1[b4]:
                            b4 += 1
                        b3 = "".join(b1[i:b4 + 1]).strip('"')
                        b2.append(b3)
                        a4 = b4
                    else:
                        b2.append(b1[i])
                try:
                    b5 = int(b2[-5])
                    b6 = float(b2[-4])
                    if b5 > a2:
                        a2 = b5
                    if b6 > a3:
                        a3 = b6
                except:
                    continue
        meta.write("a2: %d\n" % (a2))
        meta.write("a3: %f\n" % (a3))
        f.seek(0)
        for line in f.readlines():
            b1 = line.rstrip().split(',')
            if b1[0] == "world_rank":
                continue
            else:
                b2 = []
                a4 = 0
                for i in range(len(b1)):
                    if i <= a4:
                        continue
                    if '"' in b1[i]:
                        b3 = b1[i]
                        b4 = i + 1
                        while '"' not in b1[b4]:
                            b4 += 1
                        b3 = "".join(b1[i:b4 + 1]).strip('"')
                        b2.append(b3)
                        a4 = b4
                    else:
                        b2.append(b1[i])
                try:
                    b5 = float(b2[-5]) / a2
                    b6 = 1.0 - (float(b2[-4]) / a3)
                    b7 = b2[0]
                    b8 = float(b2[2]) / 100
                    b9 = b2[-6]
                    lbls.write(b7 + "\n")
                    try:
                        b9 = float(b9) / 100
                    except:
                        b9 = b8
                    pts.write(str(b9) + " " + str(b5) + " " + str(b6) + "\n")
                except:
                    continue
if b10 = = "__main__":
    fonk1()