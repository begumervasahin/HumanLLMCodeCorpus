from Mods.Math.Fp import Fp
from Mods.EC.Elliptic_Curve_Fp import EllipticCurve
from Mods.EC.Rational_Point_In_ECFp import RationalPointInEC
field_instance = Fp.get_instance(5)
print("Field instance:", field_instance)
curve_instance = EllipticCurve.get_instance(0, 1, 1)
print("Curve instance:", curve_instance)
origin_point = RationalPointInEC()
print("Origin point:", origin_point)
p1 = RationalPointInEC(0, 1)
p2 = RationalPointInEC(0, 4)
p3 = RationalPointInEC(2, 1)
p4 = RationalPointInEC(2, 4)
p5 = RationalPointInEC(3, 1)
p6 = RationalPointInEC(3, 4)
points = [p1, p2, p3, p4, p5, p6]
for i, point in enumerate(points, start=1):
    print("Point", i, ":", point)
print('Calculations:')
print("2 * Point 3:", 2 * p3)
print("Origin point + Point 1:", origin_point + p1)
print("Point 3 + Point 1:", p3 + p1)
print("Point 5 + Point 3:", p5 + p3)