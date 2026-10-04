import sys
from Memoria import Cerebro
class Memorization:
    def __init__(self, limit=10000000, cleaning_rate=0.7):
        self.memory = Cerebro(limit, cleaning_rate)
    def calculate(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        str_n1, str_n2 = str(n - 1), str(n - 2)
        n_1 = self.memory.get_lembranca(str_n1)
        n_2 = self.memory.get_lembranca(str_n2)
        if n_1 == -1:
            n_1 = self.calculate(n - 1)
            self.memory.nova_memoria(str_n1, n_1)
        if n_2 == -1:
            n_2 = self.calculate(n - 2)
            self.memory.nova_memoria(str_n2, n_2)
        return n_1 + n_2
    def get_calculation_function(self):
        return lambda n: self.calculate(n)
    def __str__(self):
        return "Recursive + Memoization"
def main():
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <number>")
        return
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Please enter a valid integer.")
        return
    fib_calculator = Memorization()
    result = fib_calculator.calculate(n)
    print(f"Fibonacci number for {n} is: {result}")
if __name__ == "__main__":
    main()