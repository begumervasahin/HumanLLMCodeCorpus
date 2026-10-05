def babylonian_square_root(number, epsilon):
    x0 = (1 + number) / 2
    x1 = (x0 + number / x0) * 0.5
    error = (x1 - x0) / x0
    if error < 0:
        error = -error
    while error > epsilon:
        x0 = x1
        x1 = (x0 + number / x0) * 0.5
        error = (x1 - x0) / x0
        if error < 0:
            error = -error
    result_message = "The square root of %s is approximately %s" % (number, x1)
    print(result_message)
def babylonian_square_root_main():
    babylonian_square_root(5, 0.00001)
babylonian_square_root_main()