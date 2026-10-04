from Mods.EC.Elliptic_Curve import EllipticCurve
from Mods.EC.Rational_Point_In_EC import RationalPointInEC
def main():
    curve = EllipticCurve.get_instance(0, -2)
    print(curve)
    o = RationalPointInEC()
    r1 = RationalPointInEC(-1, 1, curve)
    r2 = RationalPointInEC(2, 2, curve)
    print('Show values')
    print(f'o = {o}')
    print(f'r1 = {r1}')
    print(f'r2 = {r2}')
    print('Show calculations')
    print(f'r1 + o = {r1 + o}')
    print(f'r2 + r1 = {r2 + r1}')
    print(f'2 * r1 = {2 * r1}')
    print(f'4 * r1 == 3 * r1 + r1 is {4 * r1 == 3 * r1 + r1}')
if __name__ == "__main__":
    main()