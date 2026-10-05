def fibonacci_series(n):
    series = []
    a, b = 0, 1
    while b < n:
        series.append(b)
        a, b = b, a + b
    return series
def main():
    print(fibonacci_series(10))
if __name__ == '__main__':
    main()