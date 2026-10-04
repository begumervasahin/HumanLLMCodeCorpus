import random
def generate_random_numbers(filename, count, seed=0, min_value=0, max_value=99):
    random.seed(seed)
    with open(filename, 'w') as file:
        for _ in range(count):
            random_number = random.randint(min_value, max_value)
            file.write(f"{random_number}\n")
if __name__ == "__main__":
    filename = input("Enter the filename: ")
    count = int(input("Enter the number of random numbers to generate: "))
    generate_random_numbers(filename, count)