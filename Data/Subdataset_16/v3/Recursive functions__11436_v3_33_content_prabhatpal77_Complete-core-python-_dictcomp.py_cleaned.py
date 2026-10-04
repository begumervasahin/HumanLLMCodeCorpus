
b1 = {p: p * p for p in range(10)}
print("Squares (0 to 9):", b1)
b2 = {q: q ** 2 for q in range(10, 20) if q % 2 == 0}
print("Even b1 (10 to 19):", b2)
b3 = {r: r * 2 for r in range(20, 30) if r % 2 != 0}
print("Odd doubles (20 to 29):", b3)