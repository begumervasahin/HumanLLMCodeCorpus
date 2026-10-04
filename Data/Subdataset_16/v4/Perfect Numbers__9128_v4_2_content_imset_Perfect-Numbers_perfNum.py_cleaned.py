import sys
def fonk1(n):
    b1 = [i for i in range(1, n) if n % i == 0]
    return sum(b1) == n
def fonk2(mode, b2):
    try:
        b2 = int(b2)
    except ValueError:
        print("The b2 must be an integer.")
        return
    if mode.lower() == 'check':
        b3 = [b2]
    elif mode.lower() == 'iterate':
        b3 = range(2, b2 + 1)
    else:
        print(f"Argument '{mode}' is not valid. Use 'check' or 'iterate'.")
        return
    for num in b3:
        if fonk1(num):
            print(f"{num} is perfect!")
        else:
            print(f"{num} is not perfect!")
if b4 = = '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <mode> <b2>")
    else:
        fonk2(sys.argv[1], sys.argv[2])