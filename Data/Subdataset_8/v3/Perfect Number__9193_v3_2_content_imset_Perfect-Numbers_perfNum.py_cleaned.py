import sys
def is_perfect_number(number):
    factors = [1]
    for factor in range(2, number):
        if number % factor == 0:
            factors.append(factor)
    factor_sum = sum(factors)
    return factor_sum == number
def iterate_and_check(upper_limit):
    for number in range(2, upper_limit + 1):
        if is_perfect_number(number):
            print(f"{number} is perfect!")
        else:
            print(f"{number} is not perfect!")
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script_name.py [check | iterate] number")
    else:
        mode = sys.argv[1].lower()
        number = int(sys.argv[2])
        if mode == 'check':
            if is_perfect_number(number):
                print(f"{number} is perfect!")
            else:
                print(f"{number} is not perfect!")
        elif mode == 'iterate':
            iterate_and_check(number)
        else:
            print("Argument", mode, "is not valid.")