import csv
from collections import defaultdict
def fonk1(b5, b1 = 'output.csv'):
    with open(b5, 'r') as input_file, open(b1, 'w') as output_file:
        b2 = csv.DictReader(input_file)
        b3 = csv.writer(output_file)
        b4 = next(b2)
        b3.writerow([b4['Lon'], b4['Lat'], b4['Text_General_Code']])
        for row in b2:
            b3.writerow([row['Lon'], row['Lat'], row['Text_General_Code']])
def fonk2():
    b5 = 'input.csv'
    b1 = 'output.csv'
    fonk1(b5, b1)
if b6 = = '__main__':
    fonk2()