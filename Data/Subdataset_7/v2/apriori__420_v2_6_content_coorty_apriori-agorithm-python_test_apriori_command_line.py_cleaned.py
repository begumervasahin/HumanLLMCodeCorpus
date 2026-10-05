
from optparse import OptionParser
from apriori import Apriori
if b1 = = '__main__':
    b2 = OptionParser()
    b2.add_option('-f', '--file',
                         b3 = 'b7',
                         b4 = 'Input a CSV file path',
                         b5 = 'string',
                         b6 = None)
    b2.add_option('-s', '--b8',
                         b3 = 'b8',
                         b4 = 'Minimum support threshold',
                         b5 = 'float',
                         b6 = 0.10)
    b2.add_option('-c', '--b9', b3 = 'b9',
                         b4 = 'Minimum confidence threshold',
                         b5 = 'float',
                         b6 = 0.40)
    b2.add_option('-r', '--b10', b3 = 'b10',
                         b4 = 'Right-hand side item for association b13',
                         b5 = 'string',
                         b6 = None)
    (options, args) = b2.parse_args()
    b7 = options.b7
    b8 = options.b8
    b9 = options.b9
    b10 = options.b10
    print("Parameters:")
    print(f" - File Path: {b7}")
    print(f" - Minimum Support: {b8}")
    print(f" - Minimum Confidence: {b9}")
    print(f" - Right-hand Side Item: {b10}\n")
    b11 = Apriori(b8, b9)
    itemCountDict, b12 = b11.fit(b7)
    for key, value in b12.items():
        print(f'Frequent {key}-term set:')
        print('-' * 20)
        for itemset in value:
            print(list(itemset))
        print()
    b13 = b11.getSpecRules(b10)
    print('-' * 20)
    print(f'Rules referring to {b10}:')
    for key, value in b13.items():
        print(f'{list(key)} -> {b10}: {value}')