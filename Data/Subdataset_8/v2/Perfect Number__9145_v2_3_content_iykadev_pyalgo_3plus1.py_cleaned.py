def three_plus_one(x):
    count_iterations = 0
    while x > 1:
        count_iterations += 1
        if x % 2:
            x = 3 * x + 1
        else:
            x = x / 2
        print(x)
def three_plus_one_main(x):
    three_plus_one(x)
three_plus_one_main(15000)