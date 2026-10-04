18. Repository: sudhanshugupta09/MS-Apriori_Algorithm
   File: candidateGen.py
   URL: https:
   Code Content:
def fonk1(L, phi, MIS, support_count):
	a1 = 0
	b1 = []
	for l in L:
		a1 +=1
		if support_count[l] >= MIS[l]:
			for h in L[a1:]:
				if support_count[h] >= MIS[l] and abs(support_count[h] - support_count[l]) <= phi:
					b2 = l,h
					b1.append(b2)
	return b1
def fonk2(F, phi, support_count, k, MIS):
	b1 = []
	a1 = 0
	for f1 in F:
		for f2 in F:
			if f1 != f2:
				if (f1[len(f1)-1]<f2[len(f2)-1]) and (f1[:-1] == f2[:-1]) and abs(support_count[f1[len(f1)-1]] - support_count[f2[len(f2)-1]]) <= phi:
					b1.append(f1+f2[-1:])
					b3 = f1+f2[-1:]
					for k in range(1,len(b3)+1):
						b4 = b3[:k-1] + b3[k:]
						if b3[0] in b4 or MIS[b3[1]] == MIS[b3[0]]:
							if b4 not in F:
								b1.remove(b3)
								break
	return b1
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
