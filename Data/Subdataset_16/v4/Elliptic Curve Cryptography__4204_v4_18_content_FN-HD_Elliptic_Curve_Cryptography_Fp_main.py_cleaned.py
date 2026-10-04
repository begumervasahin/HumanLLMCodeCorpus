
from Mods.Math.Fp import Fp
from Mods.EC.Elliptic_Curve_Fp import EllipticCurve
from Mods.EC.Rational_Point_In_ECFp import RationalPointInEC
def fonk1():
    b1 = Fp.get_instance(5)
    print(b1)
    b2 = EllipticCurve.get_instance(0, 1, 1)
    print(b2)
    b3 = RationalPointInEC()
    b4 = RationalPointInEC(0, 1)
    b5 = RationalPointInEC(0, 4)
    b6 = RationalPointInEC(2, 1)
    b7 = RationalPointInEC(2, 4)
    b8 = RationalPointInEC(3, 1)
    b9 = RationalPointInEC(3, 4)
    b10 = [b3, b4, b5, b6, b7, b8, b9]
    for point in b10:
        print(point)
    print('Calculations:')
    print(f'2 * {b6} = {2 * b6}')
    print(f'{b3} + {b4} = {b3 + b4}')
    print(f'{b6} + {b4} = {b6 + b4}')
    print(f'{b8} + {b6} = {b8 + b6}')
if b11 = = '__main__':
    fonk1()