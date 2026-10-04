
from Mods.Math.Fp import Fp
from Mods.EC.Elliptic_Curve_Fp import EllipticCurve
from Mods.EC.Rational_Point_In_ECFp import RationalPointInEC
def main():
    fp_instance = Fp.get_instance(5)
    print("Finite Field Instance:", fp_instance)
    elliptic_curve = EllipticCurve.get_instance(0, 1, 1)
    print("Elliptic Curve Instance:", elliptic_curve)
    points = {
        "O": RationalPointInEC(),
        "P1": RationalPointInEC(0, 1),
        "P2": RationalPointInEC(0, 4),
        "P3": RationalPointInEC(2, 1),
        "P4": RationalPointInEC(2, 4),
        "P5": RationalPointInEC(3, 1),
        "P6": RationalPointInEC(3, 4)
    }
    print("\nInitialized Points:")
    for name, point in points.items():
        print(f'{name}: {point}')
    print("\nCalculations:")
    print(f'2 * P3 = {2 * points["P3"]}')
    print(f'O + P1 = {points["O"] + points["P1"]}')
    print(f'P3 + P1 = {points["P3"] + points["P1"]}')
    print(f'P5 + P3 = {points["P5"] + points["P3"]}')
if __name__ == '__main__':
    main()