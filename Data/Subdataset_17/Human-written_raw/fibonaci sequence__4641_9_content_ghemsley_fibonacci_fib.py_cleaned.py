def getInput():
    __fibNum = None
    print("Please enter the Fibonacci sequence index to find the value of: ")
    try:
        __fibNum = abs(int(input()))
    except Exception:
        print("\nThat doesn't seem like a valid entry. Please enter a positive integer.\n")
        getInput()
    return __fibNum
def fib(n):
    from math import sqrt
    __n = n
    return int(((1+sqrt(5))**__n-(1-sqrt(5))**__n)/(2**__n*sqrt(5)))
def main():
    import argparse
    from sys import exit
    __parser = argparse.ArgumentParser()
    __parser.add_argument("-i", "--index", help="Fibonacci sequence index to find value of", type=int)
    __args = __parser.parse_args()
    if __args.index is not None:
        print(str(fib(abs(int(__args.index)))))
    else:
        print("Fibonacci sequence result: " + str(fib(getInput())))
    exit()
main()