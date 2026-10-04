def check_prime(N):
    if N <= 1:
        return False
    for x in range(2, N):
        if N % x == 0:
            return False
    return True
def F(num):
    buff = []
    if num % 3 == 0 or num % 5 == 0 or num % 15 == 0 or check_prime(num):
        if num % 3 == 0:
            buff.append("Buzz")
        if num % 5 == 0:
            buff.append("Fizz")
        if num % 15 == 0:
            buff.append("FizzBuzz")
        if check_prime(num):
            buff.append("BuzzFizz")
        for item in buff:
            print(item)
    else:
        fibo = []
        a, b = 0, 1
        for i in range(num):
            if i == 0:
                fibo.append(a)
            elif i == 1:
                fibo.append(b)
            else:
                a, b = b, a + b
                fibo.append(b)
        print(fibo)
if __name__ == '__main__':
    n = int(input("How many Fibonacci numbers do you want to see? "))
    F(n)