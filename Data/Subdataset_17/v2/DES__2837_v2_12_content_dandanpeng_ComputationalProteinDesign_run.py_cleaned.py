
from function import Protein
from seqpred import Matches, genetic_algorithm
protein_ids = [
    '1aba', '1bxv', '1by2', '1hyp', '1opc',
    '1tmy', '2acy', '2mcm', '3e0e', '3k63'
]
score = 0
for protein_id in protein_ids:
    protein = Protein(protein_id)
    match = Matches(protein.match)
    genetic_algorithm(
        protein,
        match,
        100,
        50,
        2,
        0.03,
        2
    )