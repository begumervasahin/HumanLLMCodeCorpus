
def factorial(x):
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result
def digits_of_number(num):
    return [int(digit) for digit in str(num)]
def is_curious_number(num):
    return num == sum(factorial(digit) for digit in digits_of_number(num))
def find_curious_numbers(limit):
    curious_numbers = []
    for i in range(3, limit):
        if i % 100000 == 0:
            print(f"Checked up to {i} numbers...")
        if is_curious_number(i):
            curious_numbers.append(i)
    print(f"Curious numbers are: {curious_numbers}")
    print(f"There are {len(curious_numbers)} curious numbers less than {limit}.")
    return curious_numbers
if __name__ == "__main__":
    find_curious_numbers(100000000)