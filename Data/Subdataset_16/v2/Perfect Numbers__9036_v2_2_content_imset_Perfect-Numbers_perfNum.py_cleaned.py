import sys
def fonk1(num):
    b1 = [i for i in range(1, num) if num % i == 0]
    return sum(b1) == num
def fonk2(mode, b2):
    b2 = int(b2)
    if mode.lower() == 'check':
        if fonk1(b2):
            print(f"{b2} is a perfect number!")
        else:
            print(f"{b2} is not a perfect number.")
    elif mode.lower() == 'iterate':
        for num in range(2, b2 + 1):
            if fonk1(num):
                print(f"{num} is a perfect number!")
    else:
        print(f"Invalid mode: {mode}. Use 'check' to check a single number or 'iterate' to check a range of numbers.")
if b3 = = '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <mode> <b2>")
        print("mode: 'check' to check a single number, 'iterate' to check all numbers up to the b2")
        print("b2: The number to check or the upper b2 for iteration")
    else:
        fonk2(sys.argv[1], sys.argv[2])