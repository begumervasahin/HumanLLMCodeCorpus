from Memoria import Cerebro
class Memorization:
    def __init__(self):
        self.memory = Cerebro(10000000, 0.7)
    def calc_fibonacci(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        str_n1 = str(n - 1)
        str_n2 = str(n - 2)
        fib_n1 = self.memory.get_lembranca(str_n1)
        fib_n2 = self.memory.get_lembranca(str_n2)
        if fib_n1 == -1:
            fib_n1 = self.calc_fibonacci(n - 1)
            self.memory.nova_memoria(str_n1, fib_n1)
        if fib_n2 == -1:
            fib_n2 = self.calc_fibonacci(n - 2)
            self.memory.nova_memoria(str_n2, fib_n2)
        return fib_n1 + fib_n2
    def get_fibonacci_function(self):
        return lambda n: self.calc_fibonacci(n)
    def __str__(self):
        return "Recursive Fibonacci with Memoization"
if __name__ == "__main__":
    memorization = Memorization()
    n = int(input("Enter a number: "))
    result = memorization.calc_fibonacci(n)
    print("Result:", result)
