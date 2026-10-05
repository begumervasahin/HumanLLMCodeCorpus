from Mods.Math.Fp import Fp
from Mods.EC.Elliptic_Curve_Fp import EllipticCurve
from Mods.EC.Rational_Point_In_ECFp import RationalPointInEC
field_instance = Fp.get_instance(5)
print("Field instance:", field_instance)
curve_instance = EllipticCurve.get_instance(0, 1, 1)
print("Curve instance:", curve_instance)
origin_point = RationalPointInEC()
print("Origin point:", origin_point)
points = [
    RationalPointInEC(0, 1),
    RationalPointInEC(0, 4),
    RationalPointInEC(2, 1),
    RationalPointInEC(2, 4),
    RationalPointInEC(3, 1),
    RationalPointInEC(3, 4)
]
for i, point in enumerate(points, start=1):
    print(f"Point {i}:", point)
print('Calculations:')
print("2 * Point 3:", 2 * points[2])
print("Origin point + Point 1:", origin_point + points[0])
print("Point 3 + Point 1:", points[2] + points[0])
print("Point 5 + Point 3:", points[4] + points[2])