from mat import Mat
from GF2 import one
b1 = (set([1,2,3,4]), set(['b3','b6','C','D']))
b2 = {k:one for k in {(2,'b3'),(2,'C'),(2,'D'),(1,'C'),(1,'D'),(3,'b3'),(3,'D'),(4,'b3'),(4,'b6'),(4,'C'),(4,'D')}}
b3 = Mat(b1,b2)
b4 = (set([1,2,3,4]), set(['b3','b6','C','D']))
b5 = {k:one for k in {(1,'b3'),(1,'b6'),(2,'b3'),(2,'C'),(3,'b6'),(3,'C'),(3,'D'),(4,'b3')}}
b6 = Mat(b4, b5)