import sys
def fonk1(arg1, arg2):
    a1 = 0
    if arg1.lower() == 'check':
        a1 = int(arg2)
    elif arg1.lower() == 'iterate':
        a1 = 2
    else:
        print("Argument", arg1, "is not valid.")
        return
    while a1 <= int(arg2):
        b1 = []
        a2 = 1
        while a2 < a1:
            if a1 % a2 = = 0:
                b1.append(a2)
            a2 += 1
        b2 = sum(b1)
        if a2 = = b2:
            print(str(a1) + " is perfect!")
        else:
            print(str(a1) + " is not perfect!")
        if arg1.lower() == 'check':
            break
        else:
            a1 += 1
if b3 = = '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script_name.py [check | iterate] number")
    else:
        fonk1(sys.argv[1], sys.argv[2])