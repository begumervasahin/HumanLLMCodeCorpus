def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)
if __name__ == "__main__":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = gcd_recursive(num1, num2)
    print("The greatest common divisor of", num1, "and", num2, "is:", result)