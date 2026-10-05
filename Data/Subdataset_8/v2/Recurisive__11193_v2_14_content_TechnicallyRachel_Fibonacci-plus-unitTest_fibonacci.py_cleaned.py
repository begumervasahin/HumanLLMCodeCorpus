def fibonacci_sequence(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result
def main():
    print(fibonacci_sequence(10))
if __name__ == '__main__':
    main()