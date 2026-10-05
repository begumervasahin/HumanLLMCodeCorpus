4. Repository: shubhamjha97/association-rule-mining-apriori
   File: timing_wrapper.py
   URL: https:
   Code Content:
from time import time
def timeit(fn):
	def wrapper(*args, **kwargs):
		start = time()
		res = fn(*args, **kwargs)
		print(fn.__name__, "took", time() - start, "seconds.")
		return res
	return wrapper
   README Content:
Association rules mining using Apriori algorithm.
Course Assignment for CS F415- Data Mining @ BITS Pilani, Hyderabad Campus.
**Done under the guidance of Dr. Aruna Malapati, Assistant Professor, BITS Pilani, Hyderabad Campus.**
* [Introduction](
* [Data](
* [Instructions to run the scripts](
    * [Create the train matrix and the mappings](
* [Important variables](
* [Hash Function](
* [Equations used](
* [Pre-processing done](
* [Directory Structure:](
* [Prescribed format of output](
    * [Association Rules](
    * [Frequent itemsets](
* [Machine specs](
* [Results](
* [Members](
<small><i><a href='http:
Association rules mining is a rule-based method for discovering interesting relations between variables in large databases. It is intended to identify strong rules discovered in databases using some measures of interestingness. We used confidence as a measure of interestingness.
**The main purpose of this project is to get an in depth understanding of how the Apriori algorithm works.**
We implemented support counting using hash trees. The difference between out approach is significant as demonstrated by the following run times (we used the same value of ```MINSUP``` and ```MIN_CONF``` for both) -
Support counting using brute force- ```22.5s```
Support counting using hash tree- ```5.9s ```
*For the sake of comparison, we have left in the code for the brute force method commented. Please feel free to uncomment it and try it out.*
*More on [Association rule learning](https:
We used the **Groceries Market Basket Dataset**, which can be found [here](http:
Run the following command:
```python
python arm.py
```
```
MINSUP - Minimum support
HASH_DENOMINATOR - Denominator for the hash function (For support counting using hash tree)
MIN_CONF - Minimum confidence
```
We have used hash function of the followinng format-
```x(mod)k```
where k is chosen by the user.
```
confidence(X->Y) = support(X U Y) / support(X)
support(X, Y) = support count(X, Y) / total dataset size
```
The csv file was read transaction by transaction and each transaction was saved as a list.
A mapping was created from the unique items in the dataset to integers so that each item corresponded to a unique integer.
The entire data was mapped to integers to reduce the storage and computational requirement.
A reverse mapping was created from the integers to the items, so that the item names could be written in the final output file.
```
association-rule-mining-apriori/
+-- data
|   +-- groceries.csv (original data file containing transactions)
+--  arm.py(python script to read the data, mine frequent itemsets and interesting rules)
+--  hash_tree.py(python file containing the Tree and Node classes used to build the hash tree for support counting)
+--  timing_wrapper.py(python decorator used to measure execution time of functions)
+--  l_final.pkl(all the frequent itemsets in pickled format)
+--  outputs(destination to save the outputs generated)
|   +-- frequent_itemsets.txt(all the frequent itemsets presented in the prescribed format)
|   +-- association_rules.txt(all the interesting association rules mined and presented in the prescribed format)
+--  results(folder containing the results of this project)
+--  reverse_map.pkl(mapping from items to index in pickled format)
+--  requirements.txt
```
```
Precedent (itemset (support count)) ---> Antecedent (itemset (support count)) - confidence value
```
```
Frequent itemset (support count)
```
Processor: i7-7500U
Ram: 16 GB DDR4
OS: Ubuntu 16.04 LTS
| Confidence/Support | No. of itemsets | No of rules |
|---------------------|-------|--------|
| High confidence(MIN_CONF=0.5) High support count(MINSUP=60)               | 725  |  60      |
| Low confidence(MIN_CONF=0.1) High support count(MINSUP=60)              | 725   |    1189    |
| High confidence(MIN_CONF=0.5) Low support count(MINSUP=10)              | 11390   |    4187    |
| Low confidence(MIN_CONF=0.1) Low support count(MINSUP=10)              | 11390   |    35196    |
All the frequent itemsets and rules generated using the above mentioned configurations can be found in the 'results' folder.
[Shubham Jha](http:
[Praneet Mehta](http:
[Abhinav Jain](http:
