
from function import Protein
from seqpred import Matches, genetic_algorithm
protein_ids = [
    '1aba', '1bxv', '1by2', '1hyp', '1opc',
    '1tmy', '2acy', '2mcm', '3e0e', '3k63'
]
population_size = 100
num_generations = 50
tournament_size = 2
mutation_rate = 0.03
elitism_count = 2
for protein_id in protein_ids:
    protein = Protein(protein_id)
    match = Matches(protein.match)
    genetic_algorithm(
        protein,
        match,
        population_size,
        num_generations,
        tournament_size,
        mutation_rate,
        elitism_count
    )