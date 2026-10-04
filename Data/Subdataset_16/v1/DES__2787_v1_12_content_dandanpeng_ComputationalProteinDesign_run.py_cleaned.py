
from function import Protein
from seqpred import Matches, genetic_algorithm
b1 = ['1aba', '1bxv', '1by2', '1hyp', '1opc',
       '1tmy', '2acy', '2mcm', '3e0e', '3k63']
a1 = 0
for i in b1:
    b2 = Protein(i)
    b3 = Matches(b2.b3)
    genetic_algorithm(b2, b3, 100, 50, 2, 0.03, 2)