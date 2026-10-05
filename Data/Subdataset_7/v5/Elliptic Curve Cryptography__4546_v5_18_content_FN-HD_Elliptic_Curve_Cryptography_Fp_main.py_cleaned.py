from Mods.Math.Fp import Fp
from Mods.EC.Elliptic_Curve_Fp import EllipticCurve
from Mods.EC.Rational_Point_In_ECFp import RationalPointInEC
b1 = Fp.get_instance(5)
print("Field instance:", b1)
b2 = EllipticCurve.get_instance(0, 1, 1)
print("Curve instance:", b2)
b3 = RationalPointInEC()
print("Origin point:", b3)
b4 = [
    RationalPointInEC(0, 1),
    RationalPointInEC(0, 4),
    RationalPointInEC(2, 1),
    RationalPointInEC(2, 4),
    RationalPointInEC(3, 1),
    RationalPointInEC(3, 4)
]
for i, point in enumerate(b4, b5 = 1):
    print(f"Point {i}:", point)
print('Calculations:')
print("2 * Point 3:", 2 * b4[2])
print("Origin point + Point 1:", b3 + b4[0])
print("Point 3 + Point 1:", b4[2] + b4[0])
print("Point 5 + Point 3:", b4[4] + b4[2])