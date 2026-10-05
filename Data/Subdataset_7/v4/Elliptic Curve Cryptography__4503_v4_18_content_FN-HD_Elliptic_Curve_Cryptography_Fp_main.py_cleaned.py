from Mods.Math.Fp import Fp
from Mods.EC.Elliptic_Curve_Fp import EllipticCurve
from Mods.EC.Rational_Point_In_ECFp import RationalPointInEC
b1 = Fp.get_instance(5)
print("Field instance:", b1)
b2 = EllipticCurve.get_instance(0, 1, 1)
print("Curve instance:", b2)
b3 = RationalPointInEC()
print("Origin point:", b3)
b4 = RationalPointInEC(0, 1)
b5 = RationalPointInEC(0, 4)
b6 = RationalPointInEC(2, 1)
b7 = RationalPointInEC(2, 4)
b8 = RationalPointInEC(3, 1)
b9 = RationalPointInEC(3, 4)
b10 = [b4, b5, b6, b7, b8, b9]
for i, point in enumerate(b10, b11 = 1):
    print("Point", i, ":", point)
print('Calculations:')
print("2 * Point 3:", 2 * b6)
print("Origin point + Point 1:", b3 + b4)
print("Point 3 + Point 1:", b6 + b4)
print("Point 5 + Point 3:", b8 + b6)