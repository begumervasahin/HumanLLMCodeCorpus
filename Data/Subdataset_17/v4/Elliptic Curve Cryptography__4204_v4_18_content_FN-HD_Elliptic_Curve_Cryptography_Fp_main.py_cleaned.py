
from Mods.Math.Fp import Fp
from Mods.EC.Elliptic_Curve_Fp import EllipticCurve
from Mods.EC.Rational_Point_In_ECFp import RationalPointInEC
def main():
    fp_instance = Fp.get_instance(5)
    print(fp_instance)
    elliptic_curve = EllipticCurve.get_instance(0, 1, 1)
    print(elliptic_curve)
    o = RationalPointInEC()
    p1 = RationalPointInEC(0, 1)
    p2 = RationalPointInEC(0, 4)
    p3 = RationalPointInEC(2, 1)
    p4 = RationalPointInEC(2, 4)
    p5 = RationalPointInEC(3, 1)
    p6 = RationalPointInEC(3, 4)
    points = [o, p1, p2, p3, p4, p5, p6]
    for point in points:
        print(point)
    print('Calculations:')
    print(f'2 * {p3} = {2 * p3}')
    print(f'{o} + {p1} = {o + p1}')
    print(f'{p3} + {p1} = {p3 + p1}')
    print(f'{p5} + {p3} = {p5 + p3}')
if __name__ == '__main__':
    main()