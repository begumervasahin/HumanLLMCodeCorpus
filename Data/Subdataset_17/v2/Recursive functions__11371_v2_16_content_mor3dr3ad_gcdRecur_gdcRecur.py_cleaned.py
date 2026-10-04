def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)
def main():
    num1 = 48
    num2 = 18
    gcd = gcd_recursive(num1, num2)
    print(f'The GCD of {num1} and {num2} is {gcd}')
if __name__ == '__main__':
    main()