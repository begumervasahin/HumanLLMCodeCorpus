import sys
def fonk1(b6):
    b1 = [1]
    for b2 in range(2, b6):
        if b6 % b2 = = 0:
            b1.append(b2)
    b3 = sum(b1)
    return b3 = = b6
def fonk2(upper_limit):
    for b6 in range(2, upper_limit + 1):
        if fonk1(b6):
            print(f"{b6} is perfect!")
        else:
            print(f"{b6} is not perfect!")
if b4 = = '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script_name.py [check | iterate] b6")
    else:
        b5 = sys.argv[1].lower()
        b6 = int(sys.argv[2])
        if b5 = = 'check':
            if fonk1(b6):
                print(f"{b6} is perfect!")
            else:
                print(f"{b6} is not perfect!")
        elif b5 = = 'iterate':
            fonk2(b6)
        else:
            print("Argument", b5, "is not valid.")