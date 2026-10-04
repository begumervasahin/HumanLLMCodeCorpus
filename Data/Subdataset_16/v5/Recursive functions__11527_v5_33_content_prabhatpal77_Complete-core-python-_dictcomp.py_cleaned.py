
b1 = {num: num * num for num in range(10)}
print(b1)
b2 = {num: num ** 2 for num in range(10, 20) if num % 2 == 0}
print(b2)
b3 = {num: num * 2 for num in range(20, 30) if num % 2 != 0}
print(b3)