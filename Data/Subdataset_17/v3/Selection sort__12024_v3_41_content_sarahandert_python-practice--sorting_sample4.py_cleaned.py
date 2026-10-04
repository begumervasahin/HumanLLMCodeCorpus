import random
def generate_random_numbers(filename, count):
    random.seed(0)
    with open(filename, 'w') as file:
        for _ in range(count):
            number = random.randint(0, 99)
            file.write(f"{number}\n")
def get_user_input(prompt):
    return input(prompt)
def main():
    filename = get_user_input('Enter the filename: ')
    count = int(get_user_input('Enter the number of random numbers to generate: '))
    generate_random_numbers(filename, count)
    print(f"Generated {count} random numbers and saved them to {filename}")
if __name__ == "__main__":
    main()