class HashTable:
    def __init__(self, size=31):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]
    def _hash(self, key):
        if isinstance(key, int):
            return key
        elif isinstance(key, str):
            hash_code = 0
            for char in key:
                hash_code = hash_code * 31 + ord(char)
            return hash_code
        else:
            return None
    def _format_bucket(self, bucket):
        bucket_str = ""
        for key, value in bucket:
            bucket_str += f"{key}:{value}, "
        return "{" + bucket_str.rstrip(", ") + "}"
    def buckets_str(self):
        buckets_info = ""
        for i, bucket in enumerate(self.buckets):
            bucket_info = self._format_bucket(bucket)
            buckets_info += f"{str(i).zfill(4)}->{bucket_info}\n"
        return buckets_info
    def __str__(self):
        table_info = ""
        for bucket in self.buckets:
            table_info += self._format_bucket(bucket)
        return "{" + table_info.rstrip(", ") + "}"
    def put(self, key, value):
        hash_index = self._hash(key) % len(self.buckets)
        bucket = self.buckets[hash_index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, v | value)
                return
        bucket.append((key, value))
    def get(self, key):
        hash_index = self._hash(key) % len(self.buckets)
        bucket = self.buckets[hash_index]
        for k, v in bucket:
            if k == key:
                return v
        return None
    def bucket_indexof(self, key):
        hash_index = self._hash(key) % len(self.buckets)
        bucket = self.buckets[hash_index]
        return self._format_bucket(bucket)
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