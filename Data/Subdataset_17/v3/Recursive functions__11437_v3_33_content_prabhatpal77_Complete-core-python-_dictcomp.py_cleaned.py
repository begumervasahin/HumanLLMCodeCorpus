
squares = {p: p * p for p in range(10)}
print("Squares (0 to 9):", squares)
even_squares = {q: q ** 2 for q in range(10, 20) if q % 2 == 0}
print("Even squares (10 to 19):", even_squares)
odd_doubles = {r: r * 2 for r in range(20, 30) if r % 2 != 0}
print("Odd doubles (20 to 29):", odd_doubles)