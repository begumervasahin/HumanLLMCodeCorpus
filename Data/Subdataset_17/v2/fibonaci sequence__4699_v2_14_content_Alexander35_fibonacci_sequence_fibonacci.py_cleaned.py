import redis
import json
class Fibonacci:
    def __init__(self, host, db):
        self.redis = redis.StrictRedis(host=host, db=db)
        if not self.get(1):
            self.redis.set(1, 1)
            self.redis.set(2, 1)
            self.save()
    def find_nearest_left(self, n):
        if not self.get(n):
            return self.find_nearest_left(n - 1)
        return n
    def get(self, k):
        return self.redis.get(k)
    def set(self, k):
        n1 = self.get(k - 1)
        n2 = self.get(k - 2)
        self.redis.set(k, int(n1) + int(n2))
    def save(self):
        self.redis.bgsave()
    def calculate(self, start, end):
        for n in range(start, end):
            if not self.get(n):
                self.set(n)
    def numbers(self, start, end):
        if not self.get(start):
            nearest_left = self.find_nearest_left(start)
            self.numbers(nearest_left, end)
        self.calculate(start + 1, end)
    def control(self, start, end):
        return [f'<div>[{k}] == {self.get(k)}</div>' for k in range(start, end)]
def main():
    with open('config.json') as file:
        conf = json.load(file)
    fib = Fibonacci(conf['redis_host'], conf['redis_db'])
    print(fib.control(1, 50))
    fib.numbers(5, 7)
    fib.numbers(30, 40)
    fib.numbers(25, 35)
    fib.numbers(49, 50)
    print(fib.control(1, 50))
    print(fib.control(9, 13))
if __name__ == '__main__':
    main()