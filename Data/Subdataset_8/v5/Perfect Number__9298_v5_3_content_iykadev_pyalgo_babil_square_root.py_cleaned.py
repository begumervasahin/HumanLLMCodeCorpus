def babylonian_square_root(number, epsilon):
    x0 = (1 + number) / 2
    x1 = (x0 + number / x0) * 0.5
    while abs(x1 - x0) / x0 > epsilon:
        x0 = x1
        x1 = (x0 + number / x0) * 0.5
    result_message = "The square root of {} is approximately {:.5f}".format(number, x1)
    print(result_message)
def babylonian_square_root_main():
    babylonian_square_root(5, 0.00001)
babylonian_square_root_main()