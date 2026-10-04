class HashTable:
    def __init__(self):
        self.table = [None] * 10000
    def store(self, string):
        hash_value = self.calculate_hash_value(string)
        if self.table[hash_value] is None:
            self.table[hash_value] = [string]
        else:
            self.table[hash_value].append(string)
    def lookup(self, string):
        hash_value = self.calculate_hash_value(string)
        if self.table[hash_value] and string in self.table[hash_value]:
            return hash_value
        return -1
    def calculate_hash_value(self, string):
        if string:
            return ord(string[0]) * 100 + ord(string[1])
        return -1
hash_table = HashTable()
print("Hash value for 'UDACITY':", hash_table.calculate_hash_value('UDACITY'))
print("Lookup 'UDACITY' before storing:", hash_table.lookup('UDACITY'))
hash_table.store('UDACITY')
print("Lookup 'UDACITY' after storing:", hash_table.lookup('UDACITY'))
hash_table.store('UDACIOUS')
print("Lookup 'UDACIOUS' after storing:", hash_table.lookup('UDACIOUS'))