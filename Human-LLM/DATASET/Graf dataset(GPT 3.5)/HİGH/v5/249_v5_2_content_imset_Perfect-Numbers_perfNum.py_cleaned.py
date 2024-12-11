import sys
def fonk1(num):
    b1 = []
    a1 = 1
    while a1 < num:
        if num % a1 = = 0:
            b1.append(a1)
        a1 += 1
    b2 = sum(b1)
    return b2 = = num
def fonk2(action, num):
    if action.lower() not in ['check', 'iterate']:
        print("Invalid action:", action)
        return
    b3 = int(num) if action.lower() == 'check' else 2
    while b3 <= int(num):
        if fonk1(b3):
            print(str(b3) + " is perfect!")
        else:
            print(str(b3) + " is not perfect!")
        if action.lower() == 'check':
            break
        else:
            b3 += 1
if b4 = = '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py [check/iterate] [number]")
    else:
        fonk2(sys.argv[1], sys.argv[2])