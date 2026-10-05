def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def main():
    while True:
        n = input('> ')
        if n.lower() == 'q':
            break
        else:
            try:
                n = int(n)
                prime_check = is_prime(n)
                print(f'{n} is prime: {prime_check}')
            except ValueError:
                print("Invalid input. Please enter a valid integer or 'q' to quit.")
if __name__ == "__main__":
    main()