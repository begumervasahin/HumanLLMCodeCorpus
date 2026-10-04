class HashTable:
    def __init__(self, size=31):
        self.nbuckets = size
        self.the_table = [[] for _ in range(self.nbuckets)]
    def hashcode(self, key):
        if isinstance(key, int):
            return key
        elif isinstance(key, str):
            return sum(ord(char) * (31 ** idx) for idx, char in enumerate(key))
        else:
            raise TypeError("Unsupported key type")
    def buckets_str(self):
        output = []
        for i, bucket in enumerate(self.the_table):
            bucket_str = f"{str(i).zfill(4)}->" + ', '.join(f"{key}:{value}" for key, value in bucket)
            output.append(bucket_str)
        return '\n'.join(output)
    def __str__(self):
        output = ', '.join(f"{key}:{value}" for bucket in self.the_table for key, value in bucket)
        return f"{{{output}}}"
    def put(self, key, value):
        bucket_index = self.hashcode(key) % self.nbuckets
        bucket = self.the_table[bucket_index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, v | value)
                return
        bucket.append((key, value))
    def get(self, key):
        bucket_index = self.hashcode(key) % self.nbuckets
        bucket = self.the_table[bucket_index]
        for k, v in bucket:
            if k == key:
                return v
        return None
    def bucket_indexof(self, index):
        if index < 0 or index >= self.nbuckets:
            raise IndexError("Bucket index out of range")
        bucket_str = ', '.join(f"{key}:{value}" for key, value in self.the_table[index])
        return f"{{{bucket_str}}}"
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