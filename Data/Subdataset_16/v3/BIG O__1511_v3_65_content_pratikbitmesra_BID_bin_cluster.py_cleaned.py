import os
import sys
import csv
from itertools import groupby
a1 = 250
b1 = a1 * 1024 / 128
def fonk1(file_path):
    b2 = []
    b3 = []
    b4 = []
    b5 = []
    b6 = []
    with open(file_path, 'r') as extracted_csv:
        b7 = csv.b7(extracted_csv)
        next(b7)
        for row in b7:
            b6.append(int(row[0]))
            b2.append(int(row[1]))
            b3.append(int(row[2]))
            b5.append(row[3])
            b4.append(float(row[4]))
    b8 = [list(group) for _, group in groupby(b6)]
    b9 = []
    b10 = []
    b11 = []
    b12 = []
    b13 = []
    a2 = 0
    a3 = 0
    for bin_cluster in b8:
        b9.append(bin_cluster[-1])
        b10.append(len(bin_cluster))
        a2 += len(bin_cluster)
        b11.append(b4[a2 - 1])
        b13.append(b5[a2 - 1])
        b12.append(sum(b3[a3:a2]) / (2 * 1024.0))
        a3 += len(bin_cluster)
    b14 = list(zip(b9, b10, b12, b13, b11))
    b15 = file_path + '_bin_info.csv'
    with open(b15, 'w', b16 = '') as bin_info_file:
        b17 = csv.b17(bin_info_file)
        b17.writerow(["b9", "b10", "b12(MB)", "b13", "b11"])
        b17.writerows(b14)
def fonk2():
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_csv_file>")
        sys.exit(1)
    b18 = sys.argv[1]
    fonk1(b18)
if b19 = = "__main__":
    fonk2()