
from function import Protein
from seqpred import Matches, genetic_algorithm
b1 = [
    '1aba', '1bxv', '1by2', '1hyp', '1opc',
    '1tmy', '2acy', '2mcm', '3e0e', '3k63'
]
a1 = 100
a2 = 50
a3 = 2
a4 = 0.03
a5 = 2
for protein_id in b1:
    b2 = Protein(protein_id)
    b3 = Matches(b2.b3)
    genetic_algorithm(
        b2,
        b3,
        a1,
        a2,
        a3,
        a4,
        a5
    )