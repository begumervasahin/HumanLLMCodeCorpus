from Mods.EC.Elliptic_Curve import EllipticCurve
from Mods.EC.Rational_Point_In_EC import RationalPointInEC
def fonk1(b1, b2, b3):
    print('Show values')
    print(f'b1 = {b1}')
    print(f'b2 = {b2}')
    print(f'b3 = {b3}')
def fonk2(b1, b2, b3):
    print('Show calculations')
    print(f'b2 + b1 = {b2 + b1}')
    print(f'b3 + b2 = {b3 + b2}')
    print(f'2 * b2 = {2 * b2}')
    print(f'4 * b2 = = 3 * b2 + b2 is {4 * b2 == 3 * b2 + b2}')
def fonk3():
    b4 = EllipticCurve.get_instance(0, -2)
    print(b4)
    b1 = RationalPointInEC()
    b2 = RationalPointInEC(-1, 1, b4)
    b3 = RationalPointInEC(2, 2, b4)
    fonk1(b1, b2, b3)
    fonk2(b1, b2, b3)
if b5 = = "__main__":
    fonk3()