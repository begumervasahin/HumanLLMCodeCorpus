import random
def generate_nums(filename, n):
    random.seed(0)
    with open(filename, 'w') as f:
        for _ in range(n):
            f.write(f"{random.randint(0, 99)}\n")
if __name__ == "__main__":
    filename = input('Enter the filename: ')
    n = int(input('Enter the length of number list: '))
    generate_nums(filename, n)