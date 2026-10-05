
from optparse import OptionParser
from apriori import Apriori
if __name__ == '__main__':
    optParser = OptionParser()
    optParser.add_option('-f', '--file',
                         dest='filePath',
                         help='Input a CSV file path',
                         type='string',
                         default=None)
    optParser.add_option('-s', '--minSupp',
                         dest='minSupp',
                         help='Minimum support threshold',
                         type='float',
                         default=0.10)
    optParser.add_option('-c', '--minConf', dest='minConf',
                         help='Minimum confidence threshold',
                         type='float',
                         default=0.40)
    optParser.add_option('-r', '--rhs', dest='rhs',
                         help='Right-hand side item for association rules',
                         type='string',
                         default=None)
    (options, args) = optParser.parse_args()
    filePath = options.filePath
    minSupp  = options.minSupp
    minConf  = options.minConf
    rhs      = options.rhs
    print("Parameters:")
    print(f" - File Path: {filePath}")
    print(f" - Minimum Support: {minSupp}")
    print(f" - Minimum Confidence: {minConf}")
    print(f" - Right-hand Side Item: {rhs}\n")
    objApriori = Apriori(minSupp, minConf)
    itemCountDict, freqSet = objApriori.fit(filePath)
    for key, value in freqSet.items():
        print(f'Frequent {key}-term set:')
        print('-' * 20)
        for itemset in value:
            print(list(itemset))
        print()
    rules = objApriori.getSpecRules(rhs)
    print('-' * 20)
    print(f'Rules referring to {rhs}:')
    for key, value in rules.items():
        print(f'{list(key)} -> {rhs}: {value}')