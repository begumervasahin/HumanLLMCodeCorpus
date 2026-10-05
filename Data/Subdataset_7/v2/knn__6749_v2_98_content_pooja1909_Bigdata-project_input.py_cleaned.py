import csv
def fonk1(b6, b7):
    with open(b6, 'r') as input_file, open(b7, 'w') as output_file:
        b1 = csv.DictReader(input_file)
        b2 = csv.b2(output_file)
        b2.writerow(['Lon', 'Lat', 'Text_General_Code'])
        for row in b1:
            b3 = row['Lon']
            b4 = row['Lat']
            b5 = row['Text_General_Code']
            b2.writerow([b3, b4, b5])
def fonk2():
    b6 = 'input.csv'
    b7 = 'output.csv'
    fonk1(b6, b7)
if b8 = = "__main__":
    fonk2()