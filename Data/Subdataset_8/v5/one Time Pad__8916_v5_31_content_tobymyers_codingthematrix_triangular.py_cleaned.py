from vec import Vec
from vecutil import zero_vec
def triangular_solve_n(row_vectors, b):
    domain = row_vectors[0].D
    n = len(domain)
    assert domain == set(range(n))
    solution = zero_vec(domain)
    for j in reversed(range(n)):
        solution[j] = (b[j] - row_vectors[j] * solution) / row_vectors[j][j]
    return solution
def triangular_solve(row_vectors, label_list, b):
    domain = row_vectors[0].D
    solution = zero_vec(domain)
    for j in reversed(range(len(domain))):
        c = label_list[j]
        row = row_vectors[j]
        solution[c] = (b[j] - solution * row) / row[c]
    return solution