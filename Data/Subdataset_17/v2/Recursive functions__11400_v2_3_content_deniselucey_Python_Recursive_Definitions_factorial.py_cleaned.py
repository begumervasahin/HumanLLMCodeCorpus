def factorial(n):
    if n < 1:
        return 1
    else:
        result = n * factorial(n - 1)
        print(f'{n}! = {result}')
        return result
def main():
    factorial(4)
if __name__ == '__main__':
    main()