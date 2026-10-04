2. Repository: kaushiksk/multi-time-interval-apriori
   File: config.py
   URL: https:
   Code Content:
b1 = [(0, 0), (0, 3), (3, 6), (6, float('inf'))]
a1 = 0.50
b2 = [
	 [('a', 1), ('b', 3), ('c', 3), ('a', 5), ('e', 5), ('c', 10)],
	 [('d', 5), ('a', 7), ('b', 7), ('e', 7), ('d', 8), ('e', 8), ('c', 14), ('d', 15)],
	 [('a', 8), ('b', 8), ('e', 11), ('d', 12), ('b', 13), ('c', 13), ('c', 16)],
	 [('b', 15), ('f', 15), ('e', 16), ('b', 17), ('c', 17)]
	 ]
   README Content:
This is a pure python implementation of MI-Apriori Algorithm as described in "On mining multi-time-interval sequential patterns" by Ya-Han Hu et. al.[[Paper Link](https:
This was implemented as part of the Data Warehousing and Data Mining course during the 7th semester at NITK Surathkal.
As of this writing it is the only known public implementation of the algorithm.
` $ python mi-apriori.py --example 1 --minsup 0.5`
You can change the example value to 1, 2, 3 and minsup to value between 0 and 1. Execute `$ python mi-apriori.py -h` for help.
```python
from config import b2, b1
from mi-apriori import MultiTimeIntervalApriori
b3 = MultiTimeIntervalApriori(db=b2, timeIntervals=b1, min_sup=a1)
b3.run_apriori(b4 = 6, verbose=True)
```
    - Kaushik S Kalmady (@kaushiksk)
    - Siddharth V (@siddharthvdn)
