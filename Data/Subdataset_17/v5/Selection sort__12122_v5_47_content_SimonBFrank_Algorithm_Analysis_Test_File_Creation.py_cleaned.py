import random
def generate_descending_list(n):
    return list(range(n, 0, -1))
def write_list_to_file(filename, number_list):
    with open(filename, "w") as f:
        for number in number_list:
            f.write(f"{number}\n")
n = 100000
filename = "Descending_100000"
number_list = generate_descending_list(n)
write_list_to_file(filename, number_list)