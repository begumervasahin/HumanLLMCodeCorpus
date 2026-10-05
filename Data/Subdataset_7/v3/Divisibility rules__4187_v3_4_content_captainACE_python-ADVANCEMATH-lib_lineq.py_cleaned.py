def fonk1(prompt):
    b6 = int(input(f"Enter the coefficient for '{prompt}' term: "))
    b7 = int(input(f"Enter the coefficient for '{prompt}' term: "))
    b3 = int(input(f"Enter the constant term for equation {prompt}: "))
    return b6, b7, b3
def fonk2(coefficients, b3):
    a, b4 = coefficients
    if a != 0 or b4 != 0:
        print(f"{a}b13 + {b4}b5 = ", b3)
    else:
        print("Invalid equation.")
def fonk3(b15, b16):
    a1, b6 = b15
    a2, b7 = b16
    b8 = b15[2]
    b9 = b16[2]
    b10 = a1 * b7 - b6 * a2
    b11 = b8 * b7 - b6 * b9
    b12 = a1 * b9 - b8 * a2
    b13 = b11 / b10
    b5 = b12 / b10
    return b10, b11, b12, b13, b5
if b14 = = "__main__":
    print("SOLVE A LINEAR EQUATION BY CRAMER'S RULE OF DISCRIMINANTS")
    print("Equation.no.1")
    b15 = fonk1('a')
    fonk2(b15, b15[2])
    print("----------------------------")
    print("Equation.no.2")
    b16 = fonk1('k')
    fonk2(b16, b16[2])
    print("--------------------------------------------")
    print("The equation will be solved by Cramer's rule")
    b10, b11, b12, b13, b5 = fonk3(b15, b16)
    print('b10 = ', b10)
    print('b11 = ', b11)
    print('b12 = ', b12)
    print('b13 = ', b13)
    print('b5 = ', b5)