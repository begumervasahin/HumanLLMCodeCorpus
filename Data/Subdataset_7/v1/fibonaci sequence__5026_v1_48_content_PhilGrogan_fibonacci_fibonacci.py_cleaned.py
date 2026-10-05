
def fonk1(n):
    a1 = 1
    a2 = 1
    a3 = 0
    for _ in range(n - 1):
        a3 = a1 + a2
        a2 = a1
        a1 = a3
    return a1
def fonk2(b3):
    b1 = list(str(b3))
    if b1[-1] == '1' and b1[-2] != '1':
        return 'st'
    elif b1[-1] == '2' and b1[-2] != '1':
        return 'nd'
    elif b1[-1] == '3' and b1[-2] != '1':
        return 'rd'
    else:
        return 'th'
if b2 = = "__main__":
    b3 = int(input("Enter the number of the Fibonacci sequence you want displayed: "))
    b4 = fonk1(b3)
    b5 = fonk2(b3)
    print(f"{b4:,d} is the {b3:,d}{b5} number of the Fibonacci sequence.")