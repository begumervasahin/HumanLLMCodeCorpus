import csv
import itertools
import sys
def fonk1(b12):
    a1 = 250
    a2 = 128
    b1 = int((a1 * 1024) / a2)
    b2 = []
    with open(b12, 'r') as extracted_csv:
        b3 = csv.b3(extracted_csv)
        next(b3)
        b4 = None
        a3 = 0
        a4 = 0
        b5 = None
        b6 = None
        for row in b3:
            try:
                bin_num, lba, xfrlen, b6, b7 = map(int, row[:5])
            except ValueError:
                continue
            if bin_num != b4:
                if b4 is not None:
                    b8 = a4 / (2 * 1024.0)
                    b2.append((b4, a3, b8, b6, b5))
                b4 = bin_num
                a3 = 0
                a4 = 0
            a3 += 1
            a4 += xfrlen
            b5 = b7
        if b4 is not None:
            b8 = a4 / (2 * 1024.0)
            b2.append((b4, a3, b8, b6, b5))
    b9 = b12 + '_bin_info.csv'
    with open(b9, 'w', b10 = '') as bin_info_file:
        b11 = csv.b11(bin_info_file)
        b11.writerow(["bin_number", "a3", "xfrlen_bin_sum(MB)", "operation_bin", "b5"])
        b11.writerows(b2)
def fonk2():
    if len(sys.argv) != 2:
        print("Usage: python script.py <b12>")
        sys.exit(1)
    b12 = sys.argv[1]
    fonk1(b12)
if b13 = = "__main__":
    fonk2()