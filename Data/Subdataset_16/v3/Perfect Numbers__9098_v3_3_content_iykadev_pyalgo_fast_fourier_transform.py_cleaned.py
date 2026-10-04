from cmath import exp, pi
def fonk1(x):
    b1 = len(x)
    if b1 <= 1:
        return x
    b2 = fonk1(x[0::2])
    b3 = fonk1(x[1::2])
    b4 = [exp(-2j * pi * k / b1) * b3[k] for k in range(b1
    return [b2[k] + b4[k] for k in range(b1
           [b2[k] - b4[k] for k in range(b1
b5 = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]
b6 = fonk1(b5)
b7 = ' '.join(f"{abs(f):5.3f}" for f in b6)
print(b7)