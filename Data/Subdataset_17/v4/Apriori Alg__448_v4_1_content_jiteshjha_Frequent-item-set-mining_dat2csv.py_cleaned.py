import csv
import sys
def convert_dat_to_csv(source_file, destination_file):
    with open(source_file, 'r') as input_file:
        lines = input_file.readlines()
        new_lines = [line.strip().split() for line in lines]
    with open(destination_file, 'w', newline='') as output_file:
        file_writer = csv.writer(output_file)
        file_writer.writerows(new_lines)
def main():
    if len(sys.argv) != 3:
        print("Execution format: python dat2csv.py <source_file> <destination_file>")
        sys.exit(1)
    source_file = sys.argv[1]
    destination_file = sys.argv[2]
    convert_dat_to_csv(source_file, destination_file)
if __name__ == "__main__":
    main()