import sys
def fonk1(action, num):
    if action.lower() not in ['check', 'iterate']:
        print("Invalid action:", action)
        return
    b1 = int(num) if action.lower() == 'check' else 2
    while b1 <= int(num):
        b2 = []
        a1 = 1
        while a1 < b1:
            if b1 % a1 = = 0:
                b2.append(a1)
            a1 += 1
        b3 = sum(b2)
        if a1 = = b3:
            print(str(b1) + " is perfect!")
        else:
            print(str(b1) + " is not perfect!")
        if action.lower() == 'check':
            break
        else:
            b1 += 1
if b4 = = '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py [check/iterate] [number]")
    else:
        fonk1(sys.argv[1], sys.argv[2])