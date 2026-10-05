6. Repository: coorty/apriori-agorithm-python
   File: test_apriori_command_line.py
   URL: https:
   Code Content:
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
    rhs      = frozenset([options.rhs])
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
    print('rules refer to {}'.format(list(rhs)))
    for key, value in rules.items():
        print('{} -> {}: {}'.format(list(key), list(rhs), value))
   README Content:
[![Build Status](https:
An Effectively Python Implementation of Apriori Algorithm for Finding Frequent sets and Association Rules
1. data/transaction.csv: input file
2. apriori.py: define a class **Apriori**
3. test\_apriori\_command\_line.py: test the apriori algorithm
Your should input path of a csv file, which may seems like:
    Bread,Milk
	Bread,Diapers,Beer,Eggs
	Milk,Diapers,Beer,Cola
	Bread,Milk,Diapers,Beer
	Bread,Milk,Diapers,Cola
	Bread,Milk
	Bread,Cola,Beer,Milk
	Milk,Bread,Beer,Cola
	Bread,Milk,Diapers,Beer
	Bread,Beer,Diapers,Diapers
Each line is a transaction, seperated by comma (,).
To run the program with dataset provided (in ./data/) and mininum support = 0.12, mininum confidence = 0.5 and return rules for `Bread`:
	python test_apriori_command_line.py -f ./data/transaction.csv -s 0.20 -c 0.50 -r Bread
which produce results below:
	frequent 1-term set:
	--------------------
	['Diapers']
	['Beer']
	['Cola']
	['Bread']
	['Milk']
	frequent 2-term set:
	--------------------
	['Diapers', 'Beer']
	['Milk', 'Bread']
	['Diapers', 'Bread']
	['Diapers', 'Milk']
	['Bread', 'Cola']
	['Bread', 'Beer']
	['Milk', 'Cola']
	['Cola', 'Beer']
	['Milk', 'Beer']
	frequent 3-term set:
	--------------------
	['Milk', 'Cola', 'Beer']
	['Milk', 'Bread', 'Cola']
	['Milk', 'Bread', 'Beer']
	['Diapers', 'Milk', 'Bread']
	['Diapers', 'Bread', 'Beer']
	['Diapers', 'Milk', 'Beer']
	==============================
	rules refer to ['Bread']
	['Milk'] -> ['Bread']: 0.8749999999999999
	['Diapers'] -> ['Bread']: 0.8333333333333334
	['Cola'] -> ['Bread']: 0.7499999999999999
	['Beer'] -> ['Bread']: 0.8571428571428572
	['Milk', 'Cola'] -> ['Bread']: 0.7499999999999999
	['Milk', 'Beer'] -> ['Bread']: 0.8
	['Diapers', 'Milk'] -> ['Bread']: 0.7499999999999999
	['Diapers', 'Beer'] -> ['Bread']: 0.8
> *Agrawal R, Srikant R. Fast algorithms for mining association rules[C]
MIT-License
