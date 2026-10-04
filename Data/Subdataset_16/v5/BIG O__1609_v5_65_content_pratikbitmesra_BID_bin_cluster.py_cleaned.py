import os
import sys
import csv
from itertools import groupby
from operator import itemgetter
a1 = 250
b1 = (a1 * 1024 / 128)
def fonk1(filename):
    b2 = []
    b3 = []
    b4 = []
    b5 = []
    b6 = []
    with open(filename, 'r') as extracted_csv:
        b7 = csv.b7(extracted_csv)
        next(b7)
        for store_line in b7:
            try:
                b6.append(int(store_line[0]))
                b2.append(int(store_line[1]))
                b3.append(int(store_line[2]))
                b5.append(store_line[3])
                b4.append(float(store_line[4]))
            except IndexError:
                continue
    b8 = [list(v) for k, v in groupby(b6)]
    b9 = []
    b10 = []
    b11 = []
    b12 = []
    b13 = []
    a2 = 0
    a3 = 0
    for y in b8:
        b9.append(y[-1])
        b10.append(len(y))
        a2 += len(y)
        b11.append(b4[a2 - 1])
        b13.append(b5[a2 - 1])
        b12.append(sum(b3[a3:a2]) / (2 * 1024.0))
        a3 += len(y)
    b14 = zip(b9, b10, b12, b13, b11)
    b15 = f"{filename}_bin_info.csv"
    with open(b15, 'w+', b16 = '') as bin_info_file:
        bin_info_file.write("b9,b10,b12(MB),b13,b11\n")
        b17 = csv.b17(bin_info_file)
        b17.writerows(b14)
def fonk2():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <extracted_csv_file>")
        sys.exit(1)
    b18 = sys.argv[1]
    fonk1(b18)
if b19 = = "__main__":
    fonk2()