
def fonk1(n):
    a1 = 1
    a2 = 1
    for _ in range(n - 1):
        b1 = a1 + a2
        a2 = a1
        a1 = b1
    b2 = 'th'
    b3 = str(n)
    if b3[-1] == '1' and (len(b3) == 1 or b3[-2] != '1'):
        b2 = 'st'
    elif b3[-1] == '2' and (len(b3) == 1 or b3[-2] != '1'):
        b2 = 'nd'
    elif b3[-1] == '3' and (len(b3) == 1 or b3[-2] != '1'):
        b2 = 'rd'
    return a1, b2
if b4 = = "__main__":
    b5 = int(input("Enter the number of the Fibonacci sequence you want displayed: "))
    fib_number, b2 = fonk1(b5)
    print(f"The {b5}{b2} number of the Fibonacci sequence is {fib_number:,d}.")