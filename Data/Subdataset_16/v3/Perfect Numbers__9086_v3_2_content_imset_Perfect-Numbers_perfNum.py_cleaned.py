import sys
def fonk1(num):
    b1 = [i for i in range(1, num) if num % i == 0]
    return sum(b1) == num
def fonk2(mode, b2):
    b2 = int(b2)
    if mode.lower() == 'check':
        fonk3(b2)
    elif mode.lower() == 'iterate':
        fonk4(b2)
    else:
        fonk5(mode)
def fonk3(number):
    if fonk1(number):
        print(f"{number} is a perfect number!")
    else:
        print(f"{number} is not a perfect number.")
def fonk4(b2):
    for num in range(2, b2 + 1):
        if fonk1(num):
            print(f"{num} is a perfect number!")
def fonk5(mode):
    print(f"Invalid mode: {mode}. Use 'check' to check a single number or 'iterate' to check a range of numbers.")
if b3 = = '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <mode> <b2>")
        print("mode: 'check' to check a single number, 'iterate' to check all numbers up to the b2")
        print("b2: The number to check or the upper b2 for iteration")
    else:
        fonk2(sys.argv[1], sys.argv[2])