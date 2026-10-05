class MyDictionary:
    def __init__(self):
        self.dictionary = {}
    def add(self, key, value):
        self.dictionary[key] = value
    def update(self, key, value):
        self.dictionary[key] = value
    def get_dictionary(self):
        return self.dictionary
class Blocking:
    def create_hash_table(self, data):
        hash_table = MyDictionary()
        count = -1
        for index, item in enumerate(data):
            key = self.create_hash_key(item)
            count += 1
            item_with_count = f"{item},{count}"
            if key in hash_table.get_dictionary():
                hash_table.update(key, item_with_count)
            else:
                hash_table.add(key, item_with_count)
        return hash_table
    def create_hash_key(self, name):
        key = ''.join(sorted(w[0] for w in name.split()))
        return key
    def find_keys(self, key):
        size = 1 << len(key)
        num = len(key)
        lst_keys = []
        for i in range(1, size - 1):
            val = bin(i)[2:].zfill(num)
            tot = ''.join(key[j] for j in range(num) if val[j] == '1' and not key[j].isdigit())
            lst_keys.append(tot)
        return list(set(lst_keys))
if __name__ == "__main__":
    data = ["John Doe", "Jane Smith", "Alice Johnson"]
    blocking = Blocking()
    hash_table = blocking.create_hash_table(data)
    print("Hash Table:")
    print(hash_table.get_dictionary())
    key = "JhonsDoe"
    keys = blocking.find_keys(key)
    print("\nKeys for '{}' after blocking:".format(key))
    print(keys)
