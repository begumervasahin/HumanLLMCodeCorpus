from cmath import exp, pi
def fonk1(x):
    b1 = len(x)
    if b1 <= 1:
        return x
    b2 = fonk1(x[::2])
    b3 = fonk1(x[1::2])
    b4 = [exp(-2j * pi * k / b1) * b3[k] for k in range(b1
    b5 = [b2[k] + b4[k] for k in range(b1
               [b2[k] - b4[k] for k in range(b1
    return b5
b6 = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]
b7 = fonk1(b6)
b8 = ' '.join("%5.3f" % abs(f) for f in b7)
print(b8)