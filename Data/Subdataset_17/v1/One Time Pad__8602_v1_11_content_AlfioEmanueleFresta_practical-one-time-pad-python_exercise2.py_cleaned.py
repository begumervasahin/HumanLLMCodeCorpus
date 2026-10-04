
def intercept_in():
    return b'This is intercepted input.'
def intercept_out(data):
    print(f'Intercepted Output: {data}')
def main():
    x = intercept_in()
    y = x
    intercept_out(y)
if __name__ == "__main__":
    main()