import math
class Content:
    def __init__(self, key, value):
        self.key = key
        self.value = [value]
class HashTable:
    def __init__(self, size, limit, hash_method="division", collision_method="linear"):
        self.array = [None] * size
        self.size = size
        self.limit = limit
        self.count = 0
        self.keys = []
        if hash_method == "multiplication":
            self.hash_function = self._hash_multiplication
        else:
            self.hash_function = self._hash_division
        if collision_method == "quadratic":
            self.collision_function = self._collision_quadratic
        else:
            self.collision_function = self._collision_linear
    def get_array(self):
        return self.array
    def get_keys(self):
        return self.keys
    def insert_value(self, key, value):
        if len(key) < self.limit:
            return False
        numeric_key = self.hash_function(key)
        if key not in self.keys:
            self.keys.append(key)
        count = 0
        while True:
            if self.array[numeric_key] is not None:
                if self.array[numeric_key].key != key:
                    numeric_key = self.collision_function(numeric_key, count)
                    count += 1
                else:
                    self.array[numeric_key].value.append(value)
                    break
            else:
                self.array[numeric_key] = Content(key, value)
                self.count += 1
                break
        return True
    def get_value(self, key):
        if len(key) < self.limit:
            return None
        numeric_key = self.hash_function(key)
        count = 0
        while True:
            if self.array[numeric_key] is None:
                return None
            if self.array[numeric_key].key == key:
                return self.array[numeric_key].value
            numeric_key = self.collision_function(numeric_key, count)
            count = (count + 1) % self.size
    def _hash_division(self, key):
        numeric_key = sum(ord(char) for char in key[:self.limit]) % self.size
        return numeric_key
    def _hash_multiplication(self, key):
        a = (math.sqrt(5) - 1) / 2
        numeric_key = sum(ord(char) for char in key[:self.limit])
        numeric_key = math.floor(self.size * ((a * numeric_key) % 1))
        return numeric_key
    def _collision_quadratic(self, key, count):
        return (key + count * count) % self.size
    def _collision_linear(self, key, count):
        return (key + count) % self.size