import random
def generate_descending_list(size):
    return list(range(size, 0, -1))
def write_list_to_file(filename, number_list):
    with open(filename, "w") as file:
        for number in number_list:
            file.write(f"{number}\n")
if __name__ == "__main__":
    n = 100000
    filename = "Descending_100000"
    number_list = generate_descending_list(n)
    write_list_to_file(filename, number_list)