import csv
import itertools
import sys
def fonk1(b17):
    a1 = 250
    b1 = (a1 * 1024 / 128)
    b2 = []
    b3 = []
    b4 = []
    b5 = []
    b6 = []
    b7 = []
    a2 = 0
    with open(b17, 'r') as extracted_csv:
        for line in extracted_csv:
            b8 = line.strip()
            b9 = b8.split(',')
            try:
                if (a2 = = 1):
                    b6.append(int(b9[0]))
                    b2.append(int(b9[1]))
                    b3.append(int(b9[2]))
                    b5.append(b9[3])
                    b4.append(float(b9[4]))
                a2 = 1
            except IndexError:
                continue
    b7 = [list(v) for k, v in itertools.groupby(b6)]
    b10 = []
    b11 = []
    b12 = []
    b13 = []
    b14 = []
    a3 = 0
    a4 = 0
    for y in b7:
        b10.append(y[len(y) - 1])
        b11.append(len(y))
        a3 = a3 + len(y)
        b12.append(b4[a3 - 1])
        b14.append(b5[a3 - 1])
        b13.append(sum(b3[a4:a3]) / (2 * 1024.0))
        a4 = a4 + len(y)
    b15 = zip(b10, b11, b13, b14, b12)
    with open((b17 + '_bin_info.csv'), 'w+') as bin_info_file:
        bin_info_file.write("b10,b11,b13(MB),b14,b12")
        bin_info_file.write("\n")
        b16 = csv.b16(bin_info_file, delimiter=',')
        b16.writerows(b15)
def fonk2():
    b17 = sys.argv[1] if len(sys.argv) > 1 else ""
    if b17:
        fonk1(b17)
    else:
        print("Usage: python script.py b17.csv")
if b18 = = "__main__":
    fonk2()