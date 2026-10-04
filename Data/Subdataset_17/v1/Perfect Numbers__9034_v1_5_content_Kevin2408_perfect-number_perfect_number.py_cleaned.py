def find_perfect_numbers(n):
    perfect_number = 2
    while perfect_number < n:
        sum_of_divisors = 0
        b = 1
        while b < perfect_number:
            if perfect_number % b == 0:
                sum_of_divisors += b
            b += 1
        if sum_of_divisors == perfect_number:
            print(perfect_number)
        perfect_number += 1
def main():
    n = int(input("Input the range number: "))
    find_perfect_numbers(n)
if __name__ == "__main__":
    main()