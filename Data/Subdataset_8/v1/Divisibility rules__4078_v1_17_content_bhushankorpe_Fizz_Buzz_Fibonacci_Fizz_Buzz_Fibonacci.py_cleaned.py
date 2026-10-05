def check_prime(N):
    if N > 1:
        for x in range(2, N):
            if N % x == 0:
                return False
        return True
    return False
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
        for i in buff:
            print(i)
    else:
        fibo = []
        a, b = 0, 1
        for i in range(num):
            if i == 0:
                fibo.append(a)
            elif i == 1:
                fibo.append(b)
            else:
                c = a + b
                fibo.append(c)
                a, b = b, c
        print(fibo)
if __name__ == '__main__':
    print("How many Fibonacci numbers do you want to see?")
    n = int(input())
    F(n)