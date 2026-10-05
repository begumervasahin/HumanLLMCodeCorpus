6. Repository: coorty/apriori-agorithm-python
   File: test_apriori_command_line.py
   URL: https:
   Code Content:
from optparse import OptionParser
from apriori import Apriori
if b1 = = '__main__':
    b2 = OptionParser()
    b2.add_option('-f', '--file',
                         b3 = 'b7',
                         b4 = 'Input a csv file',
                         b5 = 'string',
                         b6 = None)
    b2.add_option('-s', '--b8',
                         b3 = 'b8',
                         b4 = 'Mininum b14',
                         b5 = 'float',
                         b6 = 0.10)
    b2.add_option('-c', '--b9', b3 = 'b9',
                         b4 = 'Mininum confidence',
                         b5 = 'float',
                         b6 = 0.40)
    b2.add_option('-r', '--b10', b3 = 'b10',
                         b4 = 'Right destination',
                         b5 = 'string',
                         b6 = None)
    (options, args) = b2.parse_args()
    b7 = options.b7
    b8 = options.b8
    b9 = options.b9
    b10 = frozenset([options.b10])
    print(.\
          format(b7,b8,b9, b10))
    b11 = Apriori(b8, b9)
    itemCountDict, b12 = b11.fit(b7)
    for key, value in b12.items():
        print('frequent {}-term set:'.format(key))
        print('-'*20)
        for itemset in value:
            print(list(itemset))
        print()
    b13 = b11.getSpecRules(b10)
    print('-'*20)
    print('b13 refer to {}'.format(list(b10)))
    for key, value in b13.items():
        print('{} -> {}: {}'.format(list(key), list(b10), value))
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
To run the program with dataset provided (in ./data/) and mininum b14 = 0.12, mininum confidence = 0.5 and return b13 for `Bread`:
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
	b13 refer to ['Bread']
	['Milk'] -> ['Bread']: 0.8749999999999999
	['Diapers'] -> ['Bread']: 0.8333333333333334
	['Cola'] -> ['Bread']: 0.7499999999999999
	['Beer'] -> ['Bread']: 0.8571428571428572
	['Milk', 'Cola'] -> ['Bread']: 0.7499999999999999
	['Milk', 'Beer'] -> ['Bread']: 0.8
	['Diapers', 'Milk'] -> ['Bread']: 0.7499999999999999
	['Diapers', 'Beer'] -> ['Bread']: 0.8
> *Agrawal R, Srikant R. Fast algorithms for mining association b13[C]
MIT-License
