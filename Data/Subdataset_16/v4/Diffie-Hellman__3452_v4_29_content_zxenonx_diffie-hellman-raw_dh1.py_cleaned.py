from __future__ import print_function
a1 = 23
a2 = 5
a3 = 6
a4 = 15
print("Publicly Shared Variables:")
print(f"    Prime: {a1}")
print(f"    Base:  {a2}")
b1 = pow(a2, a3, a1)
print(f"\n  Alice's Public Value (sent to Bob): {b1}")
b2 = pow(a2, a4, a1)
print(f"  Bob's Public Value (sent to Alice): {b2}")
print("\n------------\n")
print("Privately Calculated Shared Secrets:")
b3 = pow(b2, a3, a1)
print(f"    Alice's Shared Secret: {b3}")
b4 = pow(b1, a4, a1)
print(f"    Bob's Shared Secret: {b4}")