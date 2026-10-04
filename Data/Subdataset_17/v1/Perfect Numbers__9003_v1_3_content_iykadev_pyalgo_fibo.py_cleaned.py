def fibo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibo(n - 1, memo) + fibo(n - 2, memo)
    return memo[n]
def fibo_main():
    for n in range(1, 47):
        res = fibo(n)
        print(f"{n}\t{res}")
if __name__ == "__main__":
    fibo_main()