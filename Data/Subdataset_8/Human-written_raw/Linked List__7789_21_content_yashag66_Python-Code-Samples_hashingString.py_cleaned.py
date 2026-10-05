
class HashTable(object):
    def __init__(self):
        self.table = [None]*10000
    def store(self, string):
        if self.table[self.calculate_hash_value(string)] == None:
            self.table[self.calculate_hash_value(string)] = [string]
        else:
            self.table[self.calculate_hash_value(string)].append(string)
    def lookup(self, string):
        if self.table[self.calculate_hash_value(string)]:
            return self.calculate_hash_value(string)
        return -1
    def calculate_hash_value(self, string):
        if string:
            return ord(string[0]) * 100 + ord(string[1])
        return -1
hash_table = HashTable()
print hash_table.calculate_hash_value('UDACITY')
print hash_table.lookup('UDACITY')
hash_table.store('UDACITY')
print hash_table.lookup('UDACITY')
hash_table.store('UDACIOUS')
print hash_table.lookup('UDACIOUS')