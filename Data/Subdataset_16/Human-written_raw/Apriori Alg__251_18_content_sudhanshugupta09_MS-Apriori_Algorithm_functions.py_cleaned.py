18. Repository: sudhanshugupta09/MS-Apriori_Algorithm
   File: functions.py
   URL: https:
   Code Content:
import re
from operator import itemgetter
def fonk1(MIS):
	b1 = sorted(MIS.items(), key=itemgetter(1))
	return b1
def fonk2(I, MIS):
	for key, value in MIS.items():
		I.append(key)
def fonk3(b1,L,MIS,support_count):
	b2 = True
	for (i, mis_val) in b1:
		if support_count[i] >= MIS[i] and b2:
			L.append(i)
			b3 = MIS[i]
			b2 = False
		elif not b2:
			if support_count[i] >= b3:
				L.append(i)
def fonk4(F, cannot_be_together):
	b4 = [[],[],[],[],[]]
	a1 = 0
	for f in F:
		if len(f)>0:
			for s in f:
				if a1 > 0:
					for c in cannot_be_together:
						if set(c).issubset(s):
							pass
						else:
							b4[a1].append(s)
				else:
					b4[a1].append(s)
			a1+=1
	return b4
def fonk5(F, must_have):
	b5 = [[],[],[],[],[]]
	a1 = 0
	for f in F:
		if len(f)> 0:
			b4 = set()
			for s in f:
				for must in must_have:
					if a1 > 1:
						if must in s:
							b4.add(s)
							continue
					else:
						if s in must_have:
							b4.add(s)
			b5[a1-1].extend(list(b4))
		a1 += 1
	return b5
   README Content:
This is an implementation of MS-Apriori Algorithm to find frequent a3 during mining over transactional databases.
Apriori is a Data Mining Algorithm for frequent item set using association rules that learns over transactional databases. It proceeds by identifying the frequent individual items in the database and extends them to larger item sets as long as the items appear in the database often. (With certain rules/constraints to define "often"). MS-Apriori is a modified version of Apriori, but instead it uses multiple supports to satisfy the conditions extending them to larger item sets.
Is MS Apriori better? Yes! It accounts for the "rare item support." Apriori only holds 1 minimum support for the entire transaction database. In MS Apriori, we have multiple supports; every item has a min-support. This will improve the effectiveness of the association rules and account for the rare items.
**Sample Transactional Data**
{20, 30, 80, 70, 50, 90}
{20, 10, 80, 70}
{10, 20, 80}
{20, 30, 80}
{20, 80}
{20, 30, 80, 70, 50, 90, 100, 120, 140}
**Sample Parameter File**
*MIS values for all items*
MIS(10) = 0.43
MIS(20) = 0.30
MIS(30) = 0.30
MIS(40) = 0.40
MIS(50) = 0.40
MIS(60) = 0.30
MIS(70) = 0.20
MIS(80) = 0.20
MIS(90) = 0.20
MIS(100) = 0.10
MIS(120) = 0.20
MIS(140) = 0.15
*Other Parameters*
a2 = 0.1
cannot_be_together: {20, 40}, {70, 80}
must-have: 20 or 40 or 50
**Sample Output File**
Frequent 1-a3
    6 : {20}
    Total number of frequent 1-a3 = 1
Frequent 2-a3
    6 : {80, 20}
a4 = 6
    2 : {90, 50}
a4 = 2
    Total number of frequent 2-a3 = 2
