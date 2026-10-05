import sys
def fonk1(b4, b1 = False, level=0, output=sys.stdout):
    for item in b4:
        if isinstance(item, list):
            fonk1(item, b1, level + 1, output)
        else:
            if b1:
                print("\t" * level, b2 = '', b3=output)
            print(item, b3 = output)
b4 = [1, [2, [3, 4], 5], 6, [7, 8]]
fonk1(b4, b1 = True)