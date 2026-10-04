import csv
import sys
def dat_to_csv(source_file, destination_file):
    try:
        with open(source_file, 'r') as input_file:
            lines = input_file.readlines()
            new_lines = []
            for line in lines:
                new_line = line.strip().split()
                new_lines.append(new_line)
        with open(destination_file, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerows(new_lines)
        print(f"File converted successfully and saved as {destination_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python dat2csv.py <source_file> <destination_file>")
    else:
        source_file = sys.argv[1]
        destination_file = sys.argv[2]
        dat_to_csv(source_file, destination_file)