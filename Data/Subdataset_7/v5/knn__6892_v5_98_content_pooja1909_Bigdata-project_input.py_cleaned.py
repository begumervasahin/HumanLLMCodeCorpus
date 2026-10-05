import csv
def fonk1(b5, b1 = 'output.csv'):
    with open(b5, 'r') as input_file, open(b1, 'w', b2 = '') as output_file:
        b3 = csv.DictReader(input_file)
        b4 = csv.writer(output_file)
        b4.writerow(['Lon', 'Lat', 'Text_General_Code'])
        for row in b3:
            b4.writerow([row['Lon'], row['Lat'], row['Text_General_Code']])
def fonk2():
    b5 = 'input.csv'
    b1 = 'output.csv'
    fonk1(b5, b1)
if b6 = = '__main__':
    fonk2()