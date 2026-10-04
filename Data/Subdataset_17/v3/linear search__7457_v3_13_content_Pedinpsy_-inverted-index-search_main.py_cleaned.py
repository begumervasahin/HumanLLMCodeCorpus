import os
import time
class HashTable:
    def __init__(self, size, collision_method, hash_method):
        self.size = size
        self.collision_method = collision_method
        self.hash_method = hash_method
        self.table = [[] for _ in range(size)]
    def _hash_multiplication(self, key):
        A = 0.6180339887
        return int(self.size * ((hash(key) * A) % 1))
    def _hash_division(self, key):
        return hash(key) % self.size
    def _resolve_collision_linear(self, index, i):
        return (index + i) % self.size
    def _resolve_collision_quadratic(self, index, i):
        return (index + i**2) % self.size
    def _get_hash_index(self, key):
        if self.hash_method == 'multiplication':
            return self._hash_multiplication(key)
        return self._hash_division(key)
    def _resolve_collision(self, index, i):
        if self.collision_method == 'linear':
            return self._resolve_collision_linear(index, i)
        return self._resolve_collision_quadratic(index, i)
    def insert_value(self, key, value):
        index = self._get_hash_index(key)
        i = 0
        new_index = index
        while self.table[new_index]:
            if self.table[new_index][0] == key:
                self.table[new_index].append(value)
                return
            i += 1
            new_index = self._resolve_collision(index, i)
        self.table[new_index] = [key, value]
    def get_value(self, key):
        index = self._get_hash_index(key)
        i = 0
        new_index = index
        while self.table[new_index]:
            if self.table[new_index][0] == key:
                return self.table[new_index][1:]
            i += 1
            new_index = self._resolve_collision(index, i)
        return None
    def get_keys(self):
        return [entry[0] for entry in self.table if entry]
def read_folder(folder):
    paths = [os.path.join(folder, name) for name in os.listdir(folder)]
    return [file for file in paths if os.path.isfile(file)]
def clean_text(text):
    for char in [",", ".", "!", "?", "\r", "\t", "\n"]:
        text = text.replace(char, "")
    return text.lower()
def generate_index(file, file_num, hash_table):
    with open(file, 'r') as f:
        words = clean_text(f.read()).split()
    for word in words:
        count = words.count(word)
        existing_values = hash_table.get_value(word)
        if existing_values:
            if not any(value[0] == count and value[1] == file_num + 1 for value in existing_values):
                hash_table.insert_value(word, [count, file_num + 1])
        else:
            hash_table.insert_value(word, [count, file_num + 1])
hashing_methods = {
    'ML': HashTable(1000000, 'linear', 'multiplication'),
    'MQ': HashTable(1000000, 'quadratic', 'multiplication'),
    'DL': HashTable(1000000, 'linear', 'division'),
    'DQ': HashTable(1000000, 'quadratic', 'division'),
}
def process_hashing(method_key, method_desc):
    start_time = time.time()
    files = read_folder('base')
    for i, file in enumerate(files):
        generate_index(file, i, hashing_methods[method_key])
    for key in sorted(hashing_methods[method_key].get_keys()):
        values = hashing_methods[method_key].get_value(key)
        print(f"{key} {values[0][0]} {files[values[0][1] - 1]}")
    end_time = time.time()
    print(f'Time for hashing using {method_desc}: {end_time - start_time}')
if __name__ == "__main__":
    process_hashing('ML', 'multiplication method with linear collision resolution')
    process_hashing('MQ', 'multiplication method with quadratic collision resolution')
    process_hashing('DL', 'division method with linear collision resolution')
    process_hashing('DQ', 'division method with quadratic collision resolution')
    while True:
        word = input("Enter a word:\n").strip()
        result = hashing_methods['ML'].get_value(word)
        if result:
            print(result)
        else:
            print("Word not found.")