import sys
def fonk1(n):
    b1 = [i for i in range(1, n) if n % i == 0]
    return sum(b1) == n
def fonk2(b3, b2):
    try:
        b2 = int(b2)
    except ValueError:
        print("The b2 must be an integer.")
        return
    b3 = b3.lower()
    if b3 = = 'check':
        b4 = [b2]
    elif b3 = = 'iterate':
        b4 = range(2, b2 + 1)
    else:
        print(f"Argument '{b3}' is not valid. Use 'check' or 'iterate'.")
        return
    for num in b4:
        if fonk1(num):
            print(f"{num} is perfect!")
        else:
            print(f"{num} is not perfect!")
def fonk3():
    if len(sys.argv) != 3:
        print("Usage: python script.py <b3> <b2>")
    else:
        fonk2(sys.argv[1], sys.argv[2])
if b5 = = '__main__':
    fonk3()