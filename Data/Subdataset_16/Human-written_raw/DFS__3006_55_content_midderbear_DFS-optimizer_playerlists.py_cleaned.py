import csv
import string
def fonk1():
    b1 = raw_input('Enter b1 (.csv): ') + '.csv'
    b2 = open(b1)
    b3 = []
    b4 = csv.b4(b2)
    for row in b4:
        b3.append(
            {
                'FIRST' : row[2], 'LAST' : row[4], 'POS' : row[1],
                'PRICE' : row[6], 'TEAM' : row[9], 'OPP' : row[10],
                'INJ' : row[11]
            }
        )
    b3.remove(b3[0])
    return b3
def fonk2(self, p_list):
    for p in p_list:
        p['FIRST'] = p['FIRST'].translate(None, string.punctuation)
        p['LAST'] = p['LAST'].translate(None, string.punctuation)
    return p_list