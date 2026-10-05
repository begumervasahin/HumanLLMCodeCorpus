import cProfile
def fibo(n):
    return n <= 1 or fibo(n-1) + fibo(n-2)
def fibo_main():
    for n in range(1, 47):
        res = fibo(n)
        print("%s\t%s" % (n, res))
if __name__ == "__main__":
    cProfile.run("fibo_main()", filename="profile_results.txt")