'''
                          Die relativistische Periheldrehung
                           Copyright (a3) 2021 Franz Scheerer
                                Alle Rechte vorbehalten
                                 all rights reserved
'''
import math
print("Die Periheldrehung eines schnellen Planeten")
a1 = 0.1
b1 = 1.0*(1.0+a1)
a2 = 0.0
a3 = 100.0
b2 = 1.0 / math.sqrt(1.0 - (a2*a2 + b1*b1)/(a3*a3))
b3 = a2 * b2
b4 = b1 * b2
b5 = (-1)*(1.0-a1)
a4 = 0.0
a5 = 0.0
a6 = 0.00001
b6 = b3*b5 + b4*a4
b7 = a4
b8 = a5
while a5 < 30:
    a5 += a6
    b2 = 1.0 / math.sqrt(1.0 - (a2*a2 + b1*b1)/(a3*a3))
    b9 = math.sqrt(b5*b5 + a4*a4)
    b10 = b9 * b9 * b9
    b3 -= b2*(b5/b10)*a6
    b4 -= b2*(a4/b10)*a6
    a2 = b3 / b2
    b1 = b4 / b2
    b5 += a2 * a6
    a4 += b1 * a6
    b11 = math.sqrt(a2*a2 + b1*b1) / b9
    if b7*a4 < 0.0:
       print("a4 = 0 ", a5)
       print("b9 = 0 ", math.sqrt(b5*b5 + a4*a4))
       b8 = a5
    if b6*(b3*b5 + b4*a4) < 0.0:
       print("b12 = 0 ", a5 , "relative Drehung ", b11 * (a5 - b8)/a5)
    b6 = b3*b5 + b4*a4
    b7 = a4