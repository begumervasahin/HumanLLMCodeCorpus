import random
def generate_nums(filename, n):
    random.seed(0)
    with open(filename, 'w') as f:
        for _ in range(n):
            f.write(str(random.randrange(0, 100)) + "\n")
def main():
    filename = input('Enter the filename: ')
    n = int(input('Enter the length of number list: '))
    generate_nums(filename, n)
    print(f"Generated {n} random numbers and saved to {filename}")
if __name__ == "__main__":
    main()