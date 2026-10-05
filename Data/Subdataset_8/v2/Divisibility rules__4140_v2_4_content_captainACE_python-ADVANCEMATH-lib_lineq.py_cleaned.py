print("SOLVE A LINEAR EQUATION BY CRAMER'S RULE OF DISCRIMINANTS")
print("Equation.no.1")
a = int(input("Enter the coefficient for 'a' term: "))
b = int(input("Enter the coefficient for 'b' term: "))
c = int(input("Enter the constant term for equation 1: "))
if a == 0:
    print('x', '+', b, 'y', '=', c)
elif b == 0:
    print(a, 'x', '+', 'y', '=', c)
elif c == 0:
    print(a, 'x', '+', b, 'y', '=', c)
elif c != 0:
    print(a, 'x', '+', b, 'y', '=', c)
elif b != 0:
    print(a, 'x', '+', b, 'y', '=', c)
elif a != 0:
    print(a, 'x', '+', b, 'y', '=', c)
else:
    print("Invalid equation.")
print("----------------------------")
print("Equation.no.2")
k = int(input("Enter the coefficient for 'k' term: "))
l = int(input("Enter the coefficient for 'l' term: "))
m = int(input("Enter the constant term for equation 2: "))
if k == 0:
    print('x', '+', l, 'y', '=', m)
elif l == 0:
    print(k, 'x', '+', 'y', '=', m)
elif m == 0:
    print(k, 'x', '+', l, 'y', '=', m)
elif m != 0:
    print(k, 'x', '+', l, 'y', '=', m)
elif l != 0:
    print(k, 'x', '+', l, 'y', '=', m)
elif k != 0:
    print(k, 'x', '+', l, 'y', '=', m)
else:
    print("Invalid equation.")
print("--------------------------------------------")
print("The equation will be solved by Cramer's rule")
d = a * k - b * l
dx = b * l - c * m
dy = a * k - c * m
x = dx / d
y = dy / d
print('d =', d)
print('dx =', dx)
print('dy =', dy)
print('x =', x)
print('y =', y)