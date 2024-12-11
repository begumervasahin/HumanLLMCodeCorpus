from optparse import OptionParser
from apriori import Apriori
def fonk1():
    b1 = OptionParser()
    b1.add_option('-f', '--file',
                      b2 = 'b8',
                      b3 = 'Input a CSV file path',
                      b4 = 'string',
                      b5 = None)
    b1.add_option('-s', '--b9',
                      b2 = 'b9',
                      b3 = 'Minimum support threshold',
                      b4 = 'float',
                      b5 = 0.10)
    b1.add_option('-c', '--b10', b2 = 'b10',
                      b3 = 'Minimum confidence threshold',
                      b4 = 'float',
                      b5 = 0.40)
    b1.add_option('-r', '--b11', b2 = 'b11',
                      b3 = 'Right-hand side item for association b14',
                      b4 = 'string',
                      b5 = None)
    return b1.parse_args()[0]
def fonk2(b8, b9, b10, b11):
    print("Parameters:")
    print(f" - File Path: {b8}")
    print(f" - Minimum Support: {b9}")
    print(f" - Minimum Confidence: {b10}")
    print(f" - Right-hand Side Item: {b11}\n")
def fonk3(b13):
    for key, value in b13.items():
        print(f'Frequent {key}-term set:')
        print('-' * 20)
        for itemset in value:
            print(list(itemset))
        print()
def fonk4(b14, b11):
    print('-' * 20)
    print(f'Rules referring to {b11}:')
    for key, value in b14.items():
        print(f'{list(key)} -> {b11}: {value}')
if b6 = = '__main__':
    b7 = fonk1()
    b8 = b7.b8
    b9 = b7.b9
    b10 = b7.b10
    b11 = b7.b11
    fonk2(b8, b9, b10, b11)
    b12 = Apriori(b9, b10)
    itemCountDict, b13 = b12.fit(b8)
    fonk3(b13)
    b14 = b12.getSpecRules(b11)
    fonk4(b14, b11)