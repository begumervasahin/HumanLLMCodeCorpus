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
        output = ""
        for i, bucket in enumerate(self.the_table):
            output += str(i).zfill(4) + '->'
            for key, value in bucket:
                output += str(key) + ':' + str(value) + ', '
            output = output.rstrip(', ') + '\n'
        return output
    def __str__(self):
        output = '{'
        for bucket in self.the_table:
            for key, value in bucket:
                output += str(key) + ':' + str(value) + ', '
        output = output.rstrip(', ') + '}'
        return output
    def put(self, key, value):
        bucket_index = self.hashcode(key) % len(self.the_table)
        bucket = self.the_table[bucket_index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, v | value)
                return
        bucket.append((key, value))
    def get(self, key):
        bucket_index = self.hashcode(key) % len(self.the_table)
        bucket = self.the_table[bucket_index]
        for k, v in bucket:
            if k == key:
                return v
        return None
    def bucket_indexof(self, key):
        bucket_index = self.hashcode(key) % len(self.the_table)
        bucket = self.the_table[bucket_index]
        output = '{'
        for k, v in bucket:
            output += str(k) + ':' + str(v) + ', '
        output = output.rstrip(', ') + '}'
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