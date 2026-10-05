
from optparse import OptionParser
from apriori import Apriori
if __name__ == '__main__':
    optParser = OptionParser()
    optParser.add_option('-f', '--file',
                         dest='filePath',
                         help='Input a csv file',
                         type='string',
                         default=None)
    optParser.add_option('-s', '--minSupp',
                         dest='minSupp',
                         help='Mininum support',
                         type='float',
                         default=0.10)
    optParser.add_option('-c', '--minConf', dest='minConf',
                         help='Mininum confidence',
                         type='float',
                         default=0.40)
    optParser.add_option('-r', '--rhs', dest='rhs',
                         help='Right destination',
                         type='string',
                         default=None)
    (options, args) = optParser.parse_args()
    filePath = options.filePath
    minSupp  = options.minSupp
    minConf  = options.minConf
    rhs      = options.rhs
    print(.\
          format(filePath,minSupp,minConf, rhs))
    objApriori = Apriori(minSupp, minConf)
    itemCountDict, freqSet = objApriori.fit(filePath)
    for key, value in freqSet.items():
        print('frequent {}-term set:'.format(key))
        print('-'*20)
        for itemset in value:
            print(list(itemset))
        print()
    rules = objApriori.getSpecRules(rhs)
    print('-'*20)
    print('rules refer to {}'.format(rhs))
    for key, value in rules.items():
        print('{} -> {}: {}'.format(list(key), rhs, value))