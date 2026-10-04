from mat import Mat
from GF2 import one
def fonk1(domain, elements) -> Mat:
    return Mat(domain, elements)
def fonk2() -> None:
    b1 = (set([1, 2, 3, 4]), set(['b3', 'b6', 'C', 'D']))
    b2 = {
        (2, 'b3'): one, (2, 'C'): one, (2, 'D'): one,
        (1, 'C'): one, (1, 'D'): one,
        (3, 'b3'): one, (3, 'D'): one,
        (4, 'b3'): one, (4, 'b6'): one, (4, 'C'): one, (4, 'D'): one
    }
    b3 = fonk1(b1, b2)
    b4 = (set([1, 2, 3, 4]), set(['b3', 'b6', 'C', 'D']))
    b5 = {
        (1, 'b3'): one, (1, 'b6'): one,
        (2, 'b3'): one, (2, 'C'): one,
        (3, 'b6'): one, (3, 'C'): one, (3, 'D'): one,
        (4, 'b3'): one
    }
    b6 = fonk1(b4, b5)
    print("Matrix b3:")
    print(b3)
    print("\nMatrix b6:")
    print(b6)
if b7 = = "__main__":
    fonk2()