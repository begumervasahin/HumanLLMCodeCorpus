
from function import Protein
from seqpred import Matches, genetic_algorithm
PROTEIN_IDS = [
    '1aba', '1bxv', '1by2', '1hyp', '1opc',
    '1tmy', '2acy', '2mcm',
]
def process_proteins(protein_ids):
    for protein_id in protein_ids:
        protein = Protein(protein_id)
        match = Matches(protein.match)
        genetic_algorithm(
            protein,
            match,
            POPULATION_SIZE,
            NUM_GENERATIONS,
            TOURNAMENT_SIZE,
            MUTATION_RATE,
            ELITISM_COUNT
        )
if __name__ == "__main__":
    score = 0
    process_proteins(PROTEIN_IDS)q