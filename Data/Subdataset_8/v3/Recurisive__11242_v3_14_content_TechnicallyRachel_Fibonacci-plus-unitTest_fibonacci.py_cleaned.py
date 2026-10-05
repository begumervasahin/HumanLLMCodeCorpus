def generate_fibonacci_sequence(limit):
    result = []
    a, b = 0, 1
    while b < limit:
        result.append(b)
        a, b = b, a + b
    return result
def main():
    print(generate_fibonacci_sequence(10))
if __name__ == '__main__':
    main()