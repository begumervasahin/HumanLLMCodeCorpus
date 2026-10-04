import redis
import json
class Fibonacci:
    def __init__(self, host, db):
        self.redis = redis.StrictRedis(host=host, db=db)
        if not self._get(1):
            self.redis.set(1, 1)
            self.redis.set(2, 1)
            self._save()
    def _get(self, k):
        value = self.redis.get(k)
        return int(value) if value else None
    def _set(self, k):
        n1 = self._get(k - 1)
        n2 = self._get(k - 2)
        self.redis.set(k, n1 + n2)
    def _save(self):
        self.redis.bgsave()
    def _find_nearest_left(self, n):
        if not self._get(n):
            return self._find_nearest_left(n - 1)
        return n
    def _calculate(self, start, end):
        for n in range(start, end):
            if not self._get(n):
                self._set(n)
    def ensure_numbers(self, start, end):
        if not self._get(start):
            nearest_left = self._find_nearest_left(start)
            self.ensure_numbers(nearest_left, end)
        self._calculate(start + 1, end)
    def control(self, start, end):
        return [f'<div>[{k}] == {self._get(k)}</div>' for k in range(start, end)]
def main():
    with open('config.json') as file:
        conf = json.load(file)
    fib = Fibonacci(conf['redis_host'], conf['redis_db'])
    print('\n'.join(fib.control(1, 50)))
    fib.ensure_numbers(5, 7)
    fib.ensure_numbers(30, 40)
    fib.ensure_numbers(25, 35)
    fib.ensure_numbers(49, 50)
    print('\n'.join(fib.control(1, 50)))
    print('\n'.join(fib.control(9, 13)))
if __name__ == '__main__':
    main()