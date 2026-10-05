import csv
import sys
import argparse
def convert_dat_to_csv(source_file, destination_file):
    with open(source_file, 'r') as input_file:
        lines = input_file.readlines()
        formatted_lines = [line.strip().split() for line in lines]
    with open(destination_file, 'w') as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerows(formatted_lines)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert space-separated text file to CSV format")
    parser.add_argument("source_file", help="Path to the source file")
    parser.add_argument("destination_file", help="Path to the destination CSV file")
    args = parser.parse_args()
    convert_dat_to_csv(args.source_file, args.destination_file)