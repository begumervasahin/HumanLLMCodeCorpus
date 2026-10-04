
squares_dict = {num: num * num for num in range(10)}
print(squares_dict)
even_squares_dict = {num: num ** 2 for num in range(10, 20) if num % 2 == 0}
print(even_squares_dict)
odd_doubles_dict = {num: num * 2 for num in range(20, 30) if num % 2 != 0}
print(odd_doubles_dict)