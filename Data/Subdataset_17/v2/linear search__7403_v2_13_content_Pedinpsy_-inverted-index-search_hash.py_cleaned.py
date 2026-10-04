import math
class Content:
    def __init__(self, key, value):
        self.key = key
        self.value = [value]
class HashTable:
    def __init__(self, size, limit, hash_method="division", collision_method='linear'):
        self.array = [None] * size
        self.size = size
        self.limit = limit
        self.count = 0
        self.keys = []
        self.hash = self.get_value_multiplication if hash_method == 'multiplication' else self.get_value_division
        self.collision = self.get_quadratic_value if collision_method == 'quadratic' else self.get_linear_value
    def get_array(self):
        return self.array
    def get_keys(self):
        return self.keys
    def insert_value(self, key, value):
        if len(key) < self.limit:
            return False
        count = 0
        numeric_key = self.hash(key)
        if key not in self.keys:
            self.keys.append(key)
        while True:
            obj = Content(key, value)
            if self.array[numeric_key] is not None:
                if self.array[numeric_key].key != key:
                    numeric_key = self.collision(numeric_key, count)
                    count += 1
                else:
                    self.array[numeric_key].value.append(value)
                    break
            else:
                self.array[numeric_key] = obj
                self.count += 1
                break
        return True
    def get_value(self, key):
        if len(key) < self.limit:
            return None
        count = 0
        numeric_key = self.hash(key)
        while self.array[numeric_key] is not None:
            if self.array[numeric_key].key == key:
                return self.array[numeric_key].value
            else:
                numeric_key = self.collision(numeric_key, count)
                count = (count + 1) % self.size
        return None
    def get_value_division(self, key):
        numeric_key = sum(ord(key[x]) for x in range(self.limit))
        return numeric_key % self.size
    def get_value_multiplication(self, key):
        a = (math.sqrt(5) - 1) / 2
        numeric_key = sum(ord(key[x]) for x in range(self.limit))
        return int(math.floor(self.size * ((a * numeric_key) % 1)))
    def get_quadratic_value(self, key, count):
        return (key + count * count) % self.size
    def get_linear_value(self, key, addition):
        return (key + addition) % self.size
if __name__ == "__main__":
    ht = HashTable(size=10, limit=5, hash_method="division", collision_method='linear')
    ht.insert_value("apple", 1)
    ht.insert_value("banana", 2)
    print(ht.get_value("apple"))
    print(ht.get_value("banana"))
    print(ht.get_array())
    print(ht.get_keys())