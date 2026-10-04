def three_plus_one(x):
    i = 0
    while x > 1:
        i += 1
        if x % 2 == 1:
            x = 3 * x + 1
        else:
            x = x
        print(x)
def three_plus_one_main(x):
    three_plus_one(x)
if __name__ == "__main__":
    three_plus_one_main(15000)