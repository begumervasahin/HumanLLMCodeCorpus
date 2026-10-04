import random
def generate_random_number(digits):
    return ''.join(str(random.randint(0, 9)) for _ in range(digits))
def main():
    num_digits = 5
    random_number = generate_random_number(num_digits)
    print(f"Generated random number with {num_digits} digits: {random_number}")
if __name__ == "__main__":
    main()