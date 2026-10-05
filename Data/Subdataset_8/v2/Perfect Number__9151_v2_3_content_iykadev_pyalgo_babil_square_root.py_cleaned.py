def babylonian_square_root(number, epsilon):
    x0 = (1 + number) / 2
    x1 = (x0 + number / x0) * 0.5
    relative_error = abs((x1 - x0) / x0)
    while relative_error > epsilon:
        x0 = x1
        x1 = (x0 + number / x0) * 0.5
        relative_error = abs((x1 - x0) / x0)
    result_string = "The square root of {} is {}".format(number, x1)
    print(result_string)
def babylonian_square_root_main():
    babylonian_square_root(5, 1e-7)
babylonian_square_root_main()