import csv
import sys
if len(sys.argv) != 3:
    print("Execution format: python dat2csv.py <source_file> <destination_file>")
else:
    with open(sys.argv[1], 'r') as input_file:
        b1 = input_file.readlines()
        b2 = [line.strip().split() for line in b1]
    with open(sys.argv[2], 'w') as output_file:
        b3 = csv.writer(output_file)
        b3.writerows(b2)