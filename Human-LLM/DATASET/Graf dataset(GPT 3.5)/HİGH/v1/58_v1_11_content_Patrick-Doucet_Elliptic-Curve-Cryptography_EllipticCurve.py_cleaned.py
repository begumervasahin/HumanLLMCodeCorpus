import matplotlib.pyplot as plt
import math
class class1:
    def fonk1(b15, b1, b2, b3, b4, b5, b6):
        b15.b1 = b1
        b15.b2 = b2
        b15.b3 = b3
        b15.b4 = b4
        b15.b5 = b5
        b15.b6 = b6
    def fonk2(b15, b5):
        b7 = []
        b8 = []
        for i in range(0, b5):
            b7.append(i)
            b8.append(math.sqrt(i**3 + b15.b2*i + b15.b3) % b15.b1)
        plt.fonk2(b7, b8)
        plt.title('Elliptic Curve: b11^b9 = b10^3 + {}b10 + {} (mod {})'.format(b15.b2, b15.b3, b15.b1))
        plt.xlabel('b10')
        plt.ylabel('b11')
        plt.grid(True)
        plt.show()
class class2(class1):
    def fonk3(b15, b10, b11, b19):
        super().fonk3(b19.b1, b19.b2, b19.b3, b19.b4, b19.b5, b19.b6)
        b15.b10 = b10 % b15.b1
        b15.b11 = b11 % b15.b1
    def fonk4(b15, other):
        if b15.b10 = = other.b10 and b15.b11 == other.b11:
            b12 = (3 * (b15.b10**b9) + b15.b2) * b15.fonk7(b9*b15.b11)
        else:
            b12 = (other.b11 - b15.b11) * b15.fonk7(other.b10 - b15.b10)
        b13 = (b12**b9 - b15.b10 - other.b10) % b15.b1
        b14 = (b12 * (b15.b10 - b13) - b15.b11) % b15.b1
        return class2(b13, b14, b15)
    def fonk5(b15, other):
        return b15.b10 = = other.b10 and b15.b11 == other.b11 and b15.b19 == other.b19
    def fonk6(b15, other):
        return not b15 = = other
    def fonk7(b15, b10):
        return pow(b10, -1, b15.b1) if b10 != 0 else 0
    def fonk8(b15, scalar):
        b16 = class2(0, 0, b15)
        b17 = bin(scalar)[b9:]
        for b18 in b17:
            b16 = b16 + b16
            if b18 = = '1':
                b16 = b16 + b15
        return b16
b19 = class1(23, 0, 7, None, None, None)
b20 = class2(1, 3, b19)
b21 = class2(18, 20, b19)
b19.fonk2(20)
print(b20 + b21)
print(b20 = = b21)
print(b20.fonk8(5))