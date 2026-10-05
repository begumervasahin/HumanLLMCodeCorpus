
b1 = {p: p * p for p in range(10)}
print("Dictionary b1:", b1)
b2 = {q: q ** 2 for q in range(10, 20) if q % 2 == 0}
print("Dictionary b2:", b2)
b3 = {r: r * 2 for r in range(20, 30) if r % 2 != 0}
print("Dictionary b3:", b3)