import csv
import sys
def fonk1(b6, b7):
    with open(b6, 'r') as input_file:
        b1 = input_file.readlines()
        b2 = [line.strip().split() for line in b1]
    with open(b7, 'w', b3 = '') as output_file:
        b4 = csv.writer(output_file)
        b4.writerows(b2)
if b5 = = "__main__":
    if len(sys.argv) != 3:
        print("Execution format: python dat2csv.py <b6> <b7>")
    else:
        b6 = sys.argv[1]
        b7 = sys.argv[2]
        fonk1(b6, b7)