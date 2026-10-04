from mat import Mat
from GF2 import one
def main():
    Ad = (set([1, 2, 3, 4]), set(['A', 'B', 'C', 'D']))
    Af = {
        (2, 'A'): one, (2, 'C'): one, (2, 'D'): one,
        (1, 'C'): one, (1, 'D'): one,
        (3, 'A'): one, (3, 'D'): one,
        (4, 'A'): one, (4, 'B'): one, (4, 'C'): one, (4, 'D'): one
    }
    A = Mat(Ad, Af)
    Bd = (set([1, 2, 3, 4]), set(['A', 'B', 'C', 'D']))
    Bf = {
        (1, 'A'): one, (1, 'B'): one,
        (2, 'A'): one, (2, 'C'): one,
        (3, 'B'): one, (3, 'C'): one, (3, 'D'): one,
        (4, 'A'): one
    }
    B = Mat(Bd, Bf)
    print("Matrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)
if __name__ == "__main__":
    main()