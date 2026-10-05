def fonk1(b3):
    b1 = even_counter = 0
    while b3:
        if b3 & b2 = = b2:
            b1 += b2
        b3 = b3 >> b2
        if b3 & b2 = = b2:
            even_counter += b2
        b3 = b3 >> b2
    return b1, even_counter
def fonk2(b3):
    if b3 = = 0:
        return True
    elif b3 = = b2:
        return False
    odd_count, b4 = fonk1(abs(b3))
    b5 = abs(odd_count - b4)
    return fonk2(b5)
if b6 = = "__main__":
    print("Enter an integer:")
    b3 = int(input())
    if fonk2(abs(b3)):
        print("%d is divisible by 3." % b3)
    else:
        print("%d is not divisible by 3." % b3)