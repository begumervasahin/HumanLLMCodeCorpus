def fonk1(b2):
    b1 = even_counter = 0
    if b2 = = 0:
        return True
    elif b2 = = b3:
        return False
    while b2:
        if b2 & b3 = = b3:
            b1 += b3
        b2 = b2 >> b3
        if b2 & b3 = = b3:
            even_counter += b3
        b2 = b2 >> b3
    return fonk1(abs(b1 - even_counter))
if b4 = = "__main__":
    print("Enter an integer:")
    b2 = int(input())
    if fonk1(abs(b2)):
        print("%d is divisible by 3." % b2)
    else:
        print("%d is not divisible by 3." % b2)