import csv
import sys
if len(sys.argv) != 3:
    print("Execution format: python dat2csv.py <source_file> <destination_file>")
else:
    with open(sys.argv[1], 'r') as input_file:
        b1 = input_file.readlines()
        b2 = []
        for line in b1:
            b3 = line.strip().split()
            b2.append(b3)
    with open(sys.argv[2], 'w', b4 = '') as output_file:
        b5 = csv.writer(output_file)
        b5.writerows(b2)