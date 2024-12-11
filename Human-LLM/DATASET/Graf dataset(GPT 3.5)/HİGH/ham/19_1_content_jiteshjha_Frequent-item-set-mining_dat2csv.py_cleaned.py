1. Repository: jiteshjha/Frequent-item-set-mining
   File: dat2csv.py
   URL: https:
   Code Content:
import csv
import sys
if len(sys.argv) != 3:
    print "Execution format: python dat2csv.py <source_file> <destination_file>"
else:
    with open(sys.argv[1], 'r') as input_file:
        b1 = input_file.readlines()
        b2 = []
        for line in b1:
            b3 = line.strip(' ').split()
            b2.append(b3)
    with open(sys.argv[2], 'w') as output_file:
        b4 = csv.writer(output_file)
        b4.writerows(b2)
   README Content:
Apriori algorithm for discovering frequent itemsets for mining Boolean association rules.
**Motivation** : http:
**Original Paper** :
> *Rakesh Agrawal and Ramakrishnan Srikant Fast algorithms for mining association rules in large databases. Proceedings of the 20th International Conference on Very Large Data Bases, VLDB, pages 487-499, Santiago, Chile, September 1994.*
The algorithm can be executed with (Both minimum support and minimum confidence lie between [0, 1]):
    python apriori.py <data_set> <minimum_support> <minimum_confidence>
Example:
    python apriori.py datasets/retail.csv 0.3 0.6
`retail.dat` contains the (anonymized) retail market basket data from an anonymous Belgian retail store(Source: http:
Additionally, `retail.dat` was converted into `retail.csv` using `dat2csv.py` provided in the repository
