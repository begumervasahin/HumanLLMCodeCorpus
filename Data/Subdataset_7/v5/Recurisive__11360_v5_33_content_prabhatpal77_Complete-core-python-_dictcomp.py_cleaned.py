
b1 = {number: number * number for number in range(10)}
print("Dictionary of squares:", b1)
b2 = {number: number ** 2 for number in range(10, 20) if number % 2 == 0}
print("Dictionary of even squares:", b2)
b3 = {number: number * 2 for number in range(20, 30) if number % 2 != 0}
print("Dictionary of odd doubles:", b3)