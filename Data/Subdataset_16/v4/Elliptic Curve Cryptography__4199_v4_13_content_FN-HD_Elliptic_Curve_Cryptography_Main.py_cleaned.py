from Mods.EC.Elliptic_Curve import EllipticCurve
from Mods.EC.Rational_Point_In_EC import RationalPointInEC
def fonk1():
    b1 = EllipticCurve.get_instance(0, -2)
    print(b1)
    b2 = RationalPointInEC()
    b3 = RationalPointInEC(-1, 1, b1)
    b4 = RationalPointInEC(2, 2, b1)
    print('Show values')
    print(f'b2 = {b2}')
    print(f'b3 = {b3}')
    print(f'b4 = {b4}')
    print('Show calculations')
    print(f'b3 + b2 = {b3 + b2}')
    print(f'b4 + b3 = {b4 + b3}')
    print(f'2 * b3 = {2 * b3}')
    print(f'4 * b3 = = 3 * b3 + b3 is {4 * b3 == 3 * b3 + b3}')
if b5 = = "__main__":
    fonk1()