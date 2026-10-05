class Hashtable:
    def __init__(self, nbuckets):
        self.table = [[] for _ in range(nbuckets)]
    def hashcode(self, o):
        if isinstance(o, int):
            return o
        elif isinstance(o, str):
            h = 0
            for char in o:
                h = h * 31 + ord(char)
            return h
        else:
            return None
    def put(self, key, value):
        if self.table is None or len(self.table) == 0:
            return
        bucket_index = self.hashcode(key) % len(self.table)
        bucket = self.table[bucket_index]
        new_item_flag = True
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                new_value = bucket[i][1] | value
                bucket[i] = (key, new_value)
                new_item_flag = False
                break
        if new_item_flag:
            bucket.append((key, value))
    def get(self, key):
        if self.table is None or len(self.table) == 0:
            return None
        bucket_index = self.hashcode(key) % len(self.table)
        bucket = self.table[bucket_index]
        for node in bucket:
            if node[0] == key:
                return node[1]
        return None
    def __str__(self):
        if self.table is None:
            return None
        output = '{'
        for i in range(len(self.table)):
            for node in self.table[i]:
                output += str(node[0]) + ':' + str(node[1])
                output += ', '
        output = output.rstrip(', ')
        output += '}'
        return output
    def __repr__(self):
        return str(self)
    def buckets_str(self):
        if self.table is None:
            return None
        output = ""
        for i in range(len(self.table)):
            output += str(i).zfill(4)
            output += '->'
            for node in self.table[i]:
                output += str(node[0]) + ':' + str(node[1])
                output += ', '
            output = output.rstrip(', ')
            output += '\n'
        return output
ht = Hashtable(5)
ht.put("apple", 10)
ht.put("banana", 20)
ht.put("apple", 5)
print("Hashtable:", ht)
print("Buckets:", ht.buckets_str())
print("Get 'apple':", ht.get("apple"))
print("Get 'banana':", ht.get("banana"))
print("Get 'orange':", ht.get("orange"))