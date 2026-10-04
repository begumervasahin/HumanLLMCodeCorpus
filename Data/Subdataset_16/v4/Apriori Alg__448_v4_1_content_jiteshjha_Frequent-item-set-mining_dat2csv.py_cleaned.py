import csv
import sys
def fonk1(b5, b6):
    with open(b5, 'r') as input_file:
        b1 = input_file.readlines()
        b2 = [line.strip().split() for line in b1]
    with open(b6, 'w', b3 = '') as output_file:
        b4 = csv.writer(output_file)
        b4.writerows(b2)
def fonk2():
    if len(sys.argv) != 3:
        print("Execution format: python dat2csv.py <b5> <b6>")
        sys.exit(1)
    b5 = sys.argv[1]
    b6 = sys.argv[2]
    fonk1(b5, b6)
if b7 = = "__main__":
    fonk2()