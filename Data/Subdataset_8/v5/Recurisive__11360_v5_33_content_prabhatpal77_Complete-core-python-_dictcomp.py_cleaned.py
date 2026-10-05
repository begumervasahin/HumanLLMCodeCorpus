
squares_dict = {number: number * number for number in range(10)}
print("Dictionary of squares:", squares_dict)
even_squares_dict = {number: number ** 2 for number in range(10, 20) if number % 2 == 0}
print("Dictionary of even squares:", even_squares_dict)
odd_doubles_dict = {number: number * 2 for number in range(20, 30) if number % 2 != 0}
print("Dictionary of odd doubles:", odd_doubles_dict)