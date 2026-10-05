
class MyDictionary:
    def __init__(self):
        self.dictionary = {}
    def add(self, key, value):
        self.dictionary[key] = value
    def update(self, key, value):
        self.dictionary[key] = value
    def my_dictionary(self):
        return self.dictionary
class Blocking:
    def CreateHashTable(self, data):
        hash_table = MyDictionary()
        count = -1
        for d in data:
            key = self.CreateHashKey(d)
            count = count + 1
            d = d + ',' + str(count)
            if key in hash_table.my_dictionary():
                hash_table.update(key, d)
            else:
                hash_table.add(key, d)
        return hash_table
    def CreateHashKey(self, name):
        key = ''
        for w in name.split():
            key = key + w[0]
        key = ''.join(sorted(key))
        return key
    def FindKeys(self, key):
        size = 1 << len(key)
        num = len(key)
        lstKeys = []
        for i in range(1, size - 1, 1):
            val = bin(i)[2:].zfill(num)
            tot = ''
            for j in range(0, len(val)):
                if j < num and val[j] == '1':
                    if not key[j].isdigit():
                        tot = tot + key[j]
            lstKeys.append(tot)
        return list(set(lstKeys))
if __name__ == "__main__":
    data = ["John Doe", "Jane Smith", "Alice Johnson"]
    blocking = Blocking()
    hash_table = blocking.CreateHashTable(data)
    print("Hash Table:")
    print(hash_table.my_dictionary())
    key = "JhonsDoe"
    keys = blocking.FindKeys(key)
    print("\nKeys for '{}' after blocking:".format(key))
    print(keys)