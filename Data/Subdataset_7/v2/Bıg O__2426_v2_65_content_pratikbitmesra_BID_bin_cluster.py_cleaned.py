import csv
import itertools
import sys
def fonk1(b17):
    a1 = 250
    b1 = int((a1 * 1024) / 128)
    b2 = []
    b3 = []
    b4 = []
    b5 = []
    b6 = []
    b7 = False
    with open(b17, 'r') as extracted_csv:
        for line in extracted_csv:
            if b7:
                b8 = line.strip().split(',')
                try:
                    b6.append(int(b8[0]))
                    b2.append(int(b8[1]))
                    b3.append(int(b8[2]))
                    b5.append(b8[3])
                    b4.append(float(b8[4]))
                except IndexError:
                    continue
            b7 = True
    b9 = [list(v) for k, v in itertools.groupby(b6)]
    b10 = []
    b11 = []
    b12 = []
    b13 = []
    b14 = []
    a2 = 0
    a3 = 0
    for bins in b9:
        b10.append(bins[-1])
        b11.append(len(bins))
        a2 += len(bins)
        b12.append(b4[a2 - 1])
        b14.append(b5[a2 - 1])
        b13.append(sum(b3[a3:a2]) / (2 * 1024.0))
        a3 += len(bins)
    b15 = zip(b10, b11, b13, b14, b12)
    with open(b17 + '_bin_info.csv', 'w+') as bin_info_file:
        bin_info_file.write("b10,b11,b13(MB),b14,b12\n")
        b16 = csv.b16(bin_info_file, delimiter=',')
        b16.writerows(b15)
def fonk2():
    if len(sys.argv) != 2:
        print("Usage: python script.py <b17>")
        sys.exit(1)
    b17 = sys.argv[1]
    fonk1(b17)
if b18 = = "__main__":
    fonk2()