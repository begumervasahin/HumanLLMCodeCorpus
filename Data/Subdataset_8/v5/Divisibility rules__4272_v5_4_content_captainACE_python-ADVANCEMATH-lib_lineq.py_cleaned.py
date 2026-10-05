def print_equation(a, b, c):
    if a == 0:
        print('x', '+', b, 'y', '=', c)
    elif b == 0:
        print(a, 'x', '+', 'y', '=', c)
    elif c == 0:
        print(a, 'x', '+', b, 'y', '=', c)
    else:
        print(a, 'x', '+', b, 'y', '=', c)
print("SOLVE A LINEAR EQUATION BY CRAMER'S RULE OF DISCRIMINANTS")
print("Equation.no.1")
a = int(input("Enter the coefficient for 'a' term: "))
b = int(input("Enter the coefficient for 'b' term: "))
c = int(input("Enter the constant term for equation 1: "))
print_equation(a, b, c)
print("----------------------------")
print("Equation.no.2")
k = int(input("Enter the coefficient for 'k' term: "))
l = int(input("Enter the coefficient for 'l' term: "))
m = int(input("Enter the constant term for equation 2: "))
print_equation(k, l, m)
print("--------------------------------------------")
print("The equation will be solved by Cramer's rule")
d = a * k - b * l
dx = b * l - c * m
dy = a * m - c * k
x = dx / d
y = dy / d
print('d =', d)
print('dx =', dx)
print('dy =', dy)
print('x =', x)
print('y =', y)