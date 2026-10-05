
def check_divisibility(number):
    results = ""
    if number % 2 == 0:
        results += "The number is divisible by 2.\n"
    if number % 3 == 0:
        results += "The number is divisible by 3.\n"
    if number % 5 == 0:
        results += "The number is divisible by 5.\n"
    if number % 7 == 0:
        results += "The number is divisible by 7.\n"
    if not results:
        results += "The number is not divisible by 2, 3, 5, or 7.\n"
    return results
number = int(input("Please enter a number of your choice:\n"))
print(check_divisibility(number))