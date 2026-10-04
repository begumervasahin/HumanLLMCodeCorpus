import random
def generate_random_number_string(length: int) -> str:
    return ''.join(str(random.randint(0, 9)) for _ in range(length))
def main() -> None:
    length = 10
    random_number = generate_random_number_string(length)
    print(f"Random number of length {length}: {random_number}")
if __name__ == "__main__":
    main()