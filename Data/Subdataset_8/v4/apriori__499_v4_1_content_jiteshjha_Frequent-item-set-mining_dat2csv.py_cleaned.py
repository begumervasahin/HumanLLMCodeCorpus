import csv
import sys
if len(sys.argv) != 3:
    print("Execution format: python dat2csv.py <source_file> <destination_file>")
else:
    with open(sys.argv[1], 'r') as input_file:
        lines = input_file.readlines()
        formatted_lines = [line.strip().split() for line in lines]
    with open(sys.argv[2], 'w') as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerows(formatted_lines)