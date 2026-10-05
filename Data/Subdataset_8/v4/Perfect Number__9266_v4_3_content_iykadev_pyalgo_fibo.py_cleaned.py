def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
def fibo_main():
    for n in range(1, 47):
        res = fibo(n)
        print("%s\t%s" % (n, res))
fibo_main()