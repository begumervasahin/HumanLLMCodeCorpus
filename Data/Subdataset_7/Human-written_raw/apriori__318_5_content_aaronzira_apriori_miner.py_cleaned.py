5. Repository: aaronzira/apriori
   File: miner.py
   URL: https:
   Code Content:
import sys
import apriori
if len(sys.argv) < 3:
    print("Expected format: python miner.py <b1> <out file> <OPTIONAL b3> <OPTIONAL min set size>")
elif len(sys.argv) >= 3:
    b1 = sys.argv[1]
    b2 = sys.argv[2]
    try:
        b3 = int(sys.argv[3])
        b4 = int(sys.argv[4])
    except IndexError:
        b3 = 4
        b4 = 3
    print("Setting b3 to {} and minimum set size to {}.".format(b3,b4))
    b5 = apriori.APriori(b1=sys.argv[1],out=sys.argv[2])
    b5.find_frequent(b3,b4)
   README Content:
Python 3 standard library implementation of the Apriori algorithm. Expected input b1 format is one row per transaction, with space-separated integers representing items.
- Output format is \<itemset size\> \<co-occurrence frequency\> \<item 1 id\> \<item 2 id\> ... \<item n id\>
From a Python 3 shell, run:
```
python miner.py <b1 file> <output file> <(optional) support parameter> <(optional) minimum set size to consider>
```
Note that if the support parameter, minimum set size, or both are omitted, they will default to 4 and 3, respectively.
- Creates frequent_itemsets.txt file found in this repo, using included transactions.dat
```
python miner.py "./transactions.dat" "./frequent_itemsets.txt" 50 5
```
