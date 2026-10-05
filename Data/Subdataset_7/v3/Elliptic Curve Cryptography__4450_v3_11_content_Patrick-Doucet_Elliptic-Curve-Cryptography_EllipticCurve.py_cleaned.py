import matplotlib.pyplot as plt
import math
class class1:
    def fonk1(b16, prime_modulus, coefficient_a, coefficient_b, b1 = None, order=None, cofactor=None):
        b16.b2 = prime_modulus
        b16.b3 = coefficient_a
        b16.b4 = coefficient_b
        b16.b5 = b1
        b16.b6 = order
        b16.b7 = cofactor
    def fonk2(b16, num_points):
        b8 = []
        b9 = []
        for i in range(num_points):
            b8.append(i)
            b9.append(math.sqrt(i**3 + b16.b3*i + b16.b4) % b16.b2)
        plt.plot(b8, b9)
        plt.title(f'Elliptic Curve: b12^b10 = b11^3 + {b16.b3}b11 + {b16.b4} (mod {b16.b2})')
        plt.xlabel('b11')
        plt.ylabel('b12')
        plt.grid(True)
        plt.show()
class class2(class1):
    def fonk3(b16, x_coord, y_coord, b20):
        super().fonk3(b20.b2, b20.b3, b20.b4, b20.b5, b20.b6, b20.b7)
        b16.b11 = x_coord % b16.b2
        b16.b12 = y_coord % b16.b2
    def fonk4(b16, other):
        if b16.b11 = = other.b11 and b16.b12 == other.b12:
            b13 = (3 * (b16.b11**b10) + b16.b3) * b16.fonk7(b10*b16.b12)
        else:
            b13 = (other.b12 - b16.b12) * b16.fonk7(other.b11 - b16.b11)
        b14 = (b13**b10 - b16.b11 - other.b11) % b16.b2
        b15 = (b13 * (b16.b11 - b14) - b16.b12) % b16.b2
        return class2(b14, b15, b16)
    def fonk5(b16, other):
        return b16.b11 = = other.b11 and b16.b12 == other.b12 and b16.b20 == other.b20
    def fonk6(b16, other):
        return not b16 = = other
    def fonk7(b16, x_val):
        return pow(x_val, -1, b16.b2) if x_val != 0 else 0
    def fonk8(b16, scalar_val):
        b17 = class2(0, 0, b16)
        b18 = bin(scalar_val)[b10:]
        for b19 in b18:
            b17 = b17 + b17
            if b19 = = '1':
                b17 = b17 + b16
        return b17
b20 = class1(23, 0, 7)
b21 = class2(1, 3, b20)
b22 = class2(18, 20, b20)
b20.fonk2(20)
print(b21 + b22)
print(b21 = = b22)
print(b21.fonk8(5))