32. Repository: AdarshRavikumar/Apriori-Algorithm
   File: AprStub.py
   URL: https:
   Code Content:
from Apriori import Apriori
b1 = int(input("Minimum support\n"))
b2 = float(input("Minimum Confidence\n"))
b3 = int(input("Minimum Length of rules \n"))
b4 = []
for i in range(ord('a'),ord('z')+1):
    b4.append(chr(i))
import re
b5 = []
b6 = []
b7 = open('datasetUCI.txt','r')
for b8 in b7:
    b8 = b8[:-1]
    b8 = re.sub("[?\s]",'a',b8)
    b9 = b8.split(',')
    for j in b9:
        if(j in b4):
            b6.append(j)
    b5.append(b6)
    b6 = []
b5 = b5
b10 = Apriori(b5,b1,b2,b3)
   README Content:
The Apriori1.py contains the actual implementation of apriori algorithm..
makepairs() - this is used to make pairs to generate rules
ex [(a,b,c,d)]
then (a->b,c,d),(b->a,c,d),(c->a,b,d),(d->a,b,c) ,((a,b)->(c,d)),,,(taken 2 at a time at LHS)...(a,b,c->d),(b,c,d->a),,,(taken 3 at a time
it will run n-1 times
i.e we have length 4 in our case , so lhs can max be 3 items and 1 items shd be in RHS to form rules
