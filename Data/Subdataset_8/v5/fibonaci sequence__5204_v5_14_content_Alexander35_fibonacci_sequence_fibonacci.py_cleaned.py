import redis
import json
class Fibonacci:
    def __init__(self, host, db):
        self.redis = redis.StrictRedis(host=host, db=db)
        if self.get(1) is None:
            self.redis.set(1, 1)
            self.redis.set(2, 1)
            self.save()
    def find_nearest_left(self, n):
        if self.get(n) is None:
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
    def calculate(self, n1, n2):
        for n in range(n1, n2):
            n_v = self.get(n)
            if n_v is None:
                self.set(n)
    def numbers(self, n1, n2):
        l_v = self.get(n1)
        if l_v is None:
            l_n = self.find_nearest_left(n1)
            self.numbers(l_n, n2)
        self.calculate(n1 + 1, n2)
    def control(self, n1, n2):
        return ['<div>[{}] == {}</div>'.format(k, self.get(k)) for k in range(n1, n2)]
def main():
    with open('config.json') as file:
        conf = json.load(file)
    fib_instance = Fibonacci(conf['redis_host'], conf['redis_db'])
    fib_instance.control(1, 50)
    fib_instance.numbers(5, 7)
    fib_instance.numbers(30, 40)
    fib_instance.numbers(25, 35)
    fib_instance.numbers(49, 50)
    fib_instance.control(1, 50)
    print(fib_instance.control(9, 13))
if __name__ == '__main__':
    main()