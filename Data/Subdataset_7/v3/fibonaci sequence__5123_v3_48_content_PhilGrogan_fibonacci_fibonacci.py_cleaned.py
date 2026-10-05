def fonk1(n):
    a1 = 1
    a2 = 1
    for _ in range(n - 2):
        a1, a2 = a1 + a2, a1
    return a1
def fonk2(i):
    b1 = str(i)
    if b1[-1] == '1' and (len(b1) == 1 or b1[-2] != '1'):
        return 'st'
    elif b1[-1] == '2' and (len(b1) == 1 or b1[-2] != '1'):
        return 'nd'
    elif b1[-1] == '3' and (len(b1) == 1 or b1[-2] != '1'):
        return 'rd'
    else:
        return 'th'
if b2 = = "__main__":
    b3 = int(input("Enter the number of the Fibonacci sequence you want displayed: "))
    b4 = fonk1(b3)
    b5 = fonk2(b3)
    print(f"The {b3}{b5} Fibonacci number is {b4:,d}.")