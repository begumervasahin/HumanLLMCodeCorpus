def fonk1():
    b1 = None
    print("Please enter the Fibonacci sequence index to find the value of: ")
    try:
        b1 = abs(int(input()))
    except Exception:
        print("\nThat doesn't seem like a valid entry. Please enter a positive integer.\n")
        fonk1()
    return b1
def fonk2(n):
    from math import sqrt
    b2 = n
    return int(((1+sqrt(5))**b2-(1-sqrt(5))**b2)/(2**b2*sqrt(5)))
def fonk3():
    import argparse
    from sys import exit
    b3 = argparse.ArgumentParser()
    b3.add_argument("-i", "--index", b4 = "Fibonacci sequence index to find value of", type=int)
    b5 = b3.parse_args()
    if b5.index is not None:
        print(str(fonk2(abs(int(b5.index)))))
    else:
        print("Fibonacci sequence result: " + str(fonk2(fonk1())))
    exit()
fonk3()