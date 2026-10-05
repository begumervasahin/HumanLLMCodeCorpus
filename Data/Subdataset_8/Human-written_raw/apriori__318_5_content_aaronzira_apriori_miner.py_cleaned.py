5. Repository: aaronzira/apriori
   File: miner.py
   URL: https:
   Code Content:
import sys
import apriori
if len(sys.argv) < 3:
    print("Expected format: python miner.py <data> <out file> <OPTIONAL sigma> <OPTIONAL min set size>")
elif len(sys.argv) >= 3:
    data = sys.argv[1]
    out_file = sys.argv[2]
    try:
        sigma = int(sys.argv[3])
        min_set_size = int(sys.argv[4])
    except IndexError:
        sigma = 4
        min_set_size = 3
    print("Setting sigma to {} and minimum set size to {}.".format(sigma,min_set_size))
    AP = apriori.APriori(data=sys.argv[1],out=sys.argv[2])
    AP.find_frequent(sigma,min_set_size)
   README Content:
Python 3 standard library implementation of the Apriori algorithm. Expected input data format is one row per transaction, with space-separated integers representing items.
- Output format is \<itemset size\> \<co-occurrence frequency\> \<item 1 id\> \<item 2 id\> ... \<item n id\>
From a Python 3 shell, run:
```
python miner.py <data file> <output file> <(optional) support parameter> <(optional) minimum set size to consider>
```
Note that if the support parameter, minimum set size, or both are omitted, they will default to 4 and 3, respectively.
- Creates frequent_itemsets.txt file found in this repo, using included transactions.dat
```
python miner.py "./transactions.dat" "./frequent_itemsets.txt" 50 5
```
