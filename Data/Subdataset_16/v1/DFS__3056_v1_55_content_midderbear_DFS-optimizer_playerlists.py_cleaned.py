import csv
import string
def fonk1():
    b1 = input('Enter b1 (without .csv extension): ') + '.csv'
    b2 = []
    with open(b1, b3 = '') as file:
        b4 = csv.b4(file)
        next(b4)
        for row in b4:
            b5 = {
                'FIRST': row[2],
                'LAST': row[4],
                'POS': row[1],
                'PRICE': row[6],
                'TEAM': row[9],
                'OPP': row[10],
                'INJ': row[11]
            }
            b2.append(b5)
    return b2
def fonk2(b2):
    for b5 in b2:
        b5['FIRST'] = b5['FIRST'].translate(str.maketrans('', '', string.punctuation))
        b5['LAST'] = b5['LAST'].translate(str.maketrans('', '', string.punctuation))
    return b2
if b6 = = "__main__":
    b7 = fonk1()
    b7 = fonk2(b7)
    for b5 in b7:
        print(b5)