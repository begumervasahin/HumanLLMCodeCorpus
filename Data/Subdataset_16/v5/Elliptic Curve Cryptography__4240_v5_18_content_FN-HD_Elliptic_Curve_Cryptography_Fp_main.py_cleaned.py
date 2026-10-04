
from Mods.Math.Fp import Fp
from Mods.EC.Elliptic_Curve_Fp import EllipticCurve
from Mods.EC.Rational_Point_In_ECFp import RationalPointInEC
def fonk1():
    b1 = Fp.get_instance(5)
    print("Finite Field Instance:", b1)
    b2 = EllipticCurve.get_instance(0, 1, 1)
    print("Elliptic Curve Instance:", b2)
    b3 = {
        "O": RationalPointInEC(),
        "b5": RationalPointInEC(0, 1),
        "P2": RationalPointInEC(0, 4),
        "b4": RationalPointInEC(2, 1),
        "P4": RationalPointInEC(2, 4),
        "P5": RationalPointInEC(3, 1),
        "P6": RationalPointInEC(3, 4)
    }
    print("\nInitialized Points:")
    for name, point in b3.items():
        print(f'{name}: {point}')
    print("\nCalculations:")
    print(f'2 * b4 = {2 * b3["b4"]}')
    print(f'O + b5 = {b3["O"] + b3["b5"]}')
    print(f'b4 + b5 = {b3["b4"] + b3["b5"]}')
    print(f'P5 + b4 = {b3["P5"] + b3["b4"]}')
if b6 = = '__main__':
    fonk1()