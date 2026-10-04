def fonk1():
    print("SOLVE A LINEAR EQUATION BY CRAMER'S RULE OF DISCRIMINANTS")
    print("Equation no. 1")
    b1 = int(input("Number for 'b1' term: "))
    b2 = int(input("Number for 'b2' term: "))
    b3 = int(input("Number for 'b3' term: "))
    fonk2(b1, b2, b3)
    print("----------------------------")
    print("Equation no. 2")
    b4 = int(input("Number for 'b4' term: "))
    b5 = int(input("Number for 'b5' term: "))
    b6 = int(input("Number for 'b6' term: "))
    fonk2(b4, b5, b6)
    print("--------------------------------------------")
    print("The equations will be solved by Cramer's rule")
    b7 = b1 * b5 - b2 * b4
    b8 = b3 * b5 - b2 * b6
    b9 = b1 * b6 - b3 * b4
    if b7 = = 0:
        if b8 = = 0 and b9 == 0:
            print("The system has infinitely many solutions.")
        else:
            print("The system has no solution.")
    else:
        b10 = b8 / b7
        b11 = b9 / b7
        print(f'b7 = {b7}')
        print(f'b8 = {b8}')
        print(f'b9 = {b9}')
        print(f'b10 = {b10}')
        print(f'b11 = {b11}')
def fonk2(b1, b2, b3):
    if b1 = = 0:
        print(f'{b2}b11 = {b3}')
    elif b2 = = 0:
        print(f'{b1}b10 = {b3}')
    else:
        print(f'{b1}b10 + {b2}b11 = {b3}')
if b12 = = "__main__":
    fonk1()