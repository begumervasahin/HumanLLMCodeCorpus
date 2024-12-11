import csv
import sys
import argparse
def fonk1(source_file, destination_file):
    with open(source_file, 'r') as input_file:
        b1 = input_file.readlines()
        b2 = [line.strip().split() for line in b1]
    with open(destination_file, 'w') as output_file:
        b3 = csv.writer(output_file)
        b3.writerows(b2)
if b4 = = "__main__":
    b5 = argparse.ArgumentParser(description="Convert space-separated text file to CSV format")
    b5.add_argument("source_file", b6 = "Path to the source file")
    b5.add_argument("destination_file", b6 = "Path to the destination CSV file")
    b7 = b5.parse_args()
    fonk1(b7.source_file, b7.destination_file)