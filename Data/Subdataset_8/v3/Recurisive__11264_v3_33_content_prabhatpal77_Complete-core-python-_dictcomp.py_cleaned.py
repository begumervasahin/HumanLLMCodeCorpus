
x = {p: p * p for p in range(10)}
print("Dictionary x:", x)
y = {q: q ** 2 for q in range(10, 20) if q % 2 == 0}
print("Dictionary y:", y)
z = {r: r * 2 for r in range(20, 30) if r % 2 != 0}
print("Dictionary z:", z)