
from function import Protein
from seqpred import Matches, genetic_algorithm
b1 = [
    '1aba', '1bxv', '1by2', '1hyp', '1opc',
    '1tmy', '2acy', '2mcm',
]
def fonk1(protein_ids):
    for protein_id in protein_ids:
        b2 = Protein(protein_id)
        b3 = Matches(b2.b3)
        genetic_algorithm(
            b2,
            b3,
            POPULATION_SIZE,
            NUM_GENERATIONS,
            TOURNAMENT_SIZE,
            MUTATION_RATE,
            ELITISM_COUNT
        )
if b4 = = "__main__":
    a1 = 0
    fonk1(b1)q