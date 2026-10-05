import csv
import sys
def convert_dat_to_csv(source_file, destination_file):
    with open(source_file, 'r') as input_file:
        lines = input_file.readlines()
        formatted_lines = [line.strip().split() for line in lines]
    with open(destination_file, 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerows(formatted_lines)
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Execution format: python dat2csv.py <source_file> <destination_file>")
    else:
        source_file = sys.argv[1]
        destination_file = sys.argv[2]
        convert_dat_to_csv(source_file, destination_file)