import sys
def fonk1(num):
    b1 = [i for i in range(1, num) if num % i == 0]
    return sum(b1) == num
def fonk2(mode, b2):
    b2 = int(b2)
    if mode.lower() == 'check':
        b3 = b2
        if fonk1(b3):
            print(f"{b3} is perfect!")
        else:
            print(f"{b3} is not perfect!")
    elif mode.lower() == 'iterate':
        b3 = 2
        while b3 <= b2:
            if fonk1(b3):
                print(f"{b3} is perfect!")
            else:
                print(f"{b3} is not perfect!")
            b3 += 1
    else:
        print(f"Argument {mode} is not valid.")
        return
if b4 = = '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <mode> <b2>")
        print("mode: 'check' to check a single number, 'iterate' to check all numbers up to the b2")
        print("b2: The number to check or the upper b2 for iteration")
    else:
        fonk2(sys.argv[1], sys.argv[2])