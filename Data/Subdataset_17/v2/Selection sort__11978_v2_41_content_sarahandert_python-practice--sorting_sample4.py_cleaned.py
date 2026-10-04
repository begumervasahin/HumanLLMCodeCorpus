import random
def generate_nums(filename, n):
    random.seed(0)
    with open(filename, 'w') as file:
        for _ in range(n):
            file.write(f"{random.randrange(0, 100)}\n")
def main():
    filename = input('Enter the filename: ')
    n = int(input('Enter the length of the number list: '))
    generate_nums(filename, n)
    print(f"Generated {n} random numbers and saved them to {filename}")
if __name__ == "__main__":
    main()