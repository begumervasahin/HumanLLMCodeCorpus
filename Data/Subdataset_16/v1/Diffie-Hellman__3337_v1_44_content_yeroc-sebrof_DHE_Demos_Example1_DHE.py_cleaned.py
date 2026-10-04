import sys
from random import randrange
b1 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
b2 = b1[randrange(len(b1))]
b3 = b1[randrange(len(b1))]
b4 = b1[randrange(5, len(b1))]
b5 = b1[randrange(len(b1))]
b6 = pow(b5, b2, b4)
b7 = pow(b5, b3, b4)
print("Public/Shared Values")
print("b5 = ", b5)
print("b4 = ", b4)
print()
print("Private Keys")
print("b2 = ", b2)
print("b3 = ", b3)
print()
print("Public Keys")
print(f"b6 = {b6} == b5^b2 mod b4 == {b5}^{b2} mod {b4}")
print(f"b7 = {b7} == b5^b3 mod b4 == {b5}^{b3} mod {b4}")
print()
b8 = pow(b7, b2, b4)
b9 = pow(b6, b3, b4)
print(f"Alice's secret b10 = = b7^b2 mod b4 == {b7}^{b2} mod {b4} == {b8}")
print(f"Bob's secret b10 = = b6^b3 mod b4 == {b6}^{b3} mod {b4} == {b9}")