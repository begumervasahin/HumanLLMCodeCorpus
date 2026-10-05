def babylonian_square_root(number, epsilon):
    x0 = (1 + number) / 2
    x1 = (x0 + number / x0) * 0.5
    relative_error = abs((x1 - x0) / x0)
    while relative_error > epsilon:
        x0 = x1
        x1 = (x0 + number / x0) * 0.5
        relative_error = abs((x1 - x0) / x0)
    return x1
def babylonian_square_root_main():
    number = 5
    precision = 1e-7
    result = babylonian_square_root(number, precision)
    result_string = "The square root of {} is {:.10f}".format(number, result)
    print(result_string)
if __name__ == "__main__":
    babylonian_square_root_main()