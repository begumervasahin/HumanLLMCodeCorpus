import os
b1 = os.path.dirname(os.path.abspath(__file__))
b2 = os.path.join(b1, "results")
b3 = os.path.join(b1, "data")
b4 = os.path.join(b3, "image_datasets")
b5 = "images"
b6 = os.path.join(b1, "data", b5)
b7 = os.path.join(b6, "train")
b8 = os.path.join(b6, "validation")
b9 = os.path.join(b6, "test")
a1 = 247
a2 = 4101
a3 = 3
a4 = 4100
a5 = 164
b10 = a1
a6 = 25
b11 = a3
b12 = (a1, a2, a3)
b13 = (b10, a6, b11)
b14 = b13
b15 = (a5, b10, a6, b11)
a7 = 9
a8 = 90
a9 = 0.05
print("b1:", b1)
print("b2:", b2)
print("b3:", b3)
print("b4:", b4)
print("b5:", b5)
print("b6:", b6)
print("b7:", b7)
print("b8:", b8)
print("b9:", b9)
print("a7:", a7)
print("a8:", a8)
print("a1:", a1)
print("a2:", a2)
print("a3:", a3)
print("a4:", a4)
print("a5:", a5)
print("b10:", b10)
print("a6:", a6)
print("b11:", b11)
print("b12:", b12)
print("b13:", b13)
print("b14:", b14)
print("b15:", b15)
print("a9:", a9)