from mat import Mat
from GF2 import one
def create_matrix(domain, function_set):
    function_dict = {k: one for k in function_set}
    return Mat(domain, function_dict)
def main():
    domain_A = (set([1, 2, 3, 4]), set(['A', 'B', 'C', 'D']))
    domain_B = (set([1, 2, 3, 4]), set(['A', 'B', 'C', 'D']))
    entries_A = {
        (2, 'A'), (2, 'C'), (2, 'D'), (1, 'C'), (1, 'D'),
        (3, 'A'), (3, 'D'), (4, 'A'), (4, 'B'), (4, 'C'), (4, 'D')
    }
    entries_B = {
        (1, 'A'), (1, 'B'), (2, 'A'), (2, 'C'),
        (3, 'B'), (3, 'C'), (3, 'D'), (4, 'A')
    }
    A = create_matrix(domain_A, entries_A)
    B = create_matrix(domain_B, entries_B)
    print("Matrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)
if __name__ == "__main__":
    main()