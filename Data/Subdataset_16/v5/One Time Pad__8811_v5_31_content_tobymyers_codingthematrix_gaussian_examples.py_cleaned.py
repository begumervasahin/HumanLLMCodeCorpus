from mat import Mat
from GF2 import one
def fonk1(domain, function_set):
    b1 = {k: one for k in function_set}
    return Mat(domain, b1)
def fonk2():
    b2 = (set([1, 2, 3, 4]), set(['b6', 'b7', 'C', 'D']))
    b3 = (set([1, 2, 3, 4]), set(['b6', 'b7', 'C', 'D']))
    b4 = {
        (2, 'b6'), (2, 'C'), (2, 'D'), (1, 'C'), (1, 'D'),
        (3, 'b6'), (3, 'D'), (4, 'b6'), (4, 'b7'), (4, 'C'), (4, 'D')
    }
    b5 = {
        (1, 'b6'), (1, 'b7'), (2, 'b6'), (2, 'C'),
        (3, 'b7'), (3, 'C'), (3, 'D'), (4, 'b6')
    }
    b6 = fonk1(b2, b4)
    b7 = fonk1(b3, b5)
    print("Matrix b6:")
    print(b6)
    print("\nMatrix b7:")
    print(b7)
if b8 = = "__main__":
    fonk2()