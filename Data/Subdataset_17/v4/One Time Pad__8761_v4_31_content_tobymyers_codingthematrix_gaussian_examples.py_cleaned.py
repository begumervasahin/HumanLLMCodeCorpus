from mat import Mat
from GF2 import one
def create_matrix(domain, function_set):
    function_dict = {k: one for k in function_set}
    return Mat(domain, function_dict)
Ad = (set([1, 2, 3, 4]), set(['A', 'B', 'C', 'D']))
Bd = (set([1, 2, 3, 4]), set(['A', 'B', 'C', 'D']))
Af_set = {(2, 'A'), (2, 'C'), (2, 'D'), (1, 'C'), (1, 'D'),
          (3, 'A'), (3, 'D'), (4, 'A'), (4, 'B'), (4, 'C'), (4, 'D')}
Bf_set = {(1, 'A'), (1, 'B'), (2, 'A'), (2, 'C'), (3, 'B'),
          (3, 'C'), (3, 'D'), (4, 'A')}
A = create_matrix(Ad, Af_set)
B = create_matrix(Bd, Bf_set)
print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)