def fonk1():
    with open("timesData.csv", 'r') as input_file, \
         open("universities.points", 'w') as points_file, \
         open("universities.labels", 'w') as labels_file, \
         open("metadata.txt", 'w') as metadata_file:
        a1 = 0
        a2 = 0.0
        for line in input_file:
            b1 = line.strip().split(',')
            if b1[0] == "world_rank":
                continue
            b2 = []
            a3 = 0
            for i, column in enumerate(b1[a3:], a3):
                if '"' in column:
                    b3 = column
                    b4 = i + 1
                    while '"' not in b1[b4]:
                        b4 += 1
                    b3 = "".join(b1[i:b4 + 1]).strip('"')
                    b2.append(b3)
                    a3 = b4
                else:
                    b2.append(column)
            try:
                b5 = int(b2[-5])
                b6 = float(b2[-4])
                a1 = max(a1, b5)
                a2 = max(a2, b6)
            except ValueError:
                continue
        metadata_file.write("a1: %d\n" % a1)
        metadata_file.write("a2: %f\n" % a2)
        input_file.seek(0)
        for line in input_file:
            b1 = line.strip().split(',')
            if b1[0] == "world_rank":
                continue
            b2 = []
            a3 = 0
            for i, column in enumerate(b1[a3:], a3):
                if '"' in column:
                    b3 = column
                    b4 = i + 1
                    while '"' not in b1[b4]:
                        b4 += 1
                    b3 = "".join(b1[i:b4 + 1]).strip('"')
                    b2.append(b3)
                    a3 = b4
                else:
                    b2.append(column)
            try:
                b5 = float(b2[-5]) / a1
                b6 = 1.0 - (float(b2[-4]) / a2)
                b7 = b2[0]
                b8 = float(b2[2]) / 100
                b9 = b2[-6]
                labels_file.write(b7 + "\n")
                try:
                    b9 = float(b9) / 100
                except ValueError:
                    b9 = b8
                points_file.write(f"{b9} {b5} {b6}\n")
            except ValueError:
                continue
if b10 = = "__main__":
    fonk1()