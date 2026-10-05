class HashTable:
    def __init__(self, size=31):
        self.nbuckets = size
        self.the_table = [[] for _ in range(self.nbuckets)]
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
    def buckets_str(self):
        if self.the_table is None:
            return None
        output = ""
        for i, bucket in enumerate(self.the_table):
            output += f"{str(i).zfill(4)}->"
            output += ', '.join([f"{node[0]}:{node[1]}" for node in bucket])
            output += '\n'
        return output
    def __str__(self):
        if self.the_table is None:
            return None
        output = '{'
        for bucket in self.the_table:
            for node in bucket:
                output += f"{node[0]}:{node[1]}, "
        output = output.rstrip(', ')
        output += '}'
        return output
    def put(self, key, value):
        if self.the_table is None or len(self.the_table) == 0:
            return
        bucket_index = self.hashcode(key) % len(self.the_table)
        bucket = self.the_table[bucket_index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, v | value)
                break
        else:
            bucket.append((key, value))
    def get(self, key):
        if self.the_table is None or len(self.the_table) == 0:
            return None
        bucket_index = self.hashcode(key) % len(self.the_table)
        bucket = self.the_table[bucket_index]
        for k, v in bucket:
            if k == key:
                return v
        return None
    def bucket_indexof(self, key):
        if self.the_table is None or len(self.the_table) == 0:
            return None
        output = '{'
        for k, v in self.the_table[key]:
            output += f"{k}:{v}, "
        output = output.rstrip(', ')
        output += '}'
        return output
    def __getitem__(self, key):
        return self.get(key)
    def __setitem__(self, key, value):
        self.put(key, value)
if __name__ == '__main__':
    h = HashTable()
    h['a'] = 34
    print(h['a'])
    table = HashTable(5)
    for i in range(1, 11):
        table.put(i, i)
    print(table.bucket_indexof(0))