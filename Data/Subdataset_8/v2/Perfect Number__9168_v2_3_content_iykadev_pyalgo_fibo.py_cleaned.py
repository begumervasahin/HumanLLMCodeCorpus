import cProfile
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
def fibonacci_main():
    for n in range(1, 47):
        result = fibonacci(n)
        print("%s\t%s" % (n, result))
if __name__ == "__main__":
    cProfile.run("fibonacci_main()", filename="profile_results.txt")