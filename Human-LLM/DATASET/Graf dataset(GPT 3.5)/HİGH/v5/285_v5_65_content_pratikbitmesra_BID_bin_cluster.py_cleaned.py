import csv
import itertools
import sys
def fonk1(b18):
    a1 = 250
    b1 = int(a1 * 1024 / 128)
    b2 = []
    b3 = []
    b4 = []
    b5 = []
    b6 = []
    b7 = []
    b8 = False
    with open(b18, 'r') as extracted_csv:
        for line in extracted_csv:
            b9 = line.strip()
            b10 = b9.split(',')
            try:
                if b8:
                    b6.append(int(b10[0]))
                    b2.append(int(b10[1]))
                    b3.append(int(b10[2]))
                    b5.append(b10[3])
                    b4.append(float(b10[4]))
                b8 = True
            except IndexError:
                continue
    b7 = [list(v) for k, v in itertools.groupby(b6)]
    b11 = []
    b12 = []
    b13 = []
    b14 = []
    b15 = []
    a2 = 0
    a3 = 0
    for y in b7:
        b11.append(y[-1])
        b12.append(len(y))
        a2 += len(y)
        b13.append(b4[a2 - 1])
        b15.append(b5[a2 - 1])
        b14.append(sum(b3[a3:a2]) / (2 * 1024.0))
        a3 += len(y)
    b16 = zip(b11, b12, b14, b15, b13)
    with open((b18 + '_bin_info.csv'), 'w+') as bin_info_file:
        bin_info_file.write("b11,b12,b14(MB),b15,b13\n")
        b17 = csv.b17(bin_info_file, delimiter=',')
        b17.writerows(b16)
def fonk2():
    b18 = sys.argv[1] if len(sys.argv) > 1 else ""
    if b18:
        fonk1(b18)
    else:
        print("Usage: python script.py b18.csv")
if b19 = = "__main__":
    fonk2()