import csv
import sys
def fonk1(b7, b8):
    try:
        with open(b7, 'r') as input_file:
            b1 = input_file.readlines()
            b2 = []
            for line in b1:
                b3 = line.strip(' ').split()
                b2.append(b3)
        with open(b8, 'w', b4 = '') as output_file:
            b5 = csv.writer(output_file)
            b5.writerows(b2)
        print(f"File converted successfully and saved as {b8}")
    except Exception as e:
        print(f"An error occurred: {e}")
if b6 = = "__main__":
    if len(sys.argv) != 3:
        print("Execution format: python dat2csv.py <b7> <b8>")
    else:
        b7 = sys.argv[1]
        b8 = sys.argv[2]
        fonk1(b7, b8)