
__author__ = 's'
with open("distance_matrix_1698.csv", "r+") as file:
    lines = [next(file).strip() for _ in range(5)]
values = lines[-1].split(",")
length_plus_1698 = len(values) + 1698
print(length_plus_1698)
third_value = values[2]
print(third_value)