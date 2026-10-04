class Hashtable:
    def __init__(self, nbuckets):
        self.buckets = [[] for _ in range(nbuckets)]
    def _hash(self, key):
        if isinstance(key, int):
            return key
        elif isinstance(key, str):
            hash_val = 0
            for char in key:
                hash_val = hash_val * 31 + ord(char)
            return hash_val
        else:
            raise TypeError("Keys must be either int or str")
    def put(self, key, value):
        index = self._hash(key) % len(self.buckets)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
    def get(self, key):
        index = self._hash(key) % len(self.buckets)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return None
    def __str__(self):
        pairs = [f"{k}:{v}" for bucket in self.buckets for k, v in bucket]
        return "{" + ", ".join(pairs) + "}"
    def __repr__(self):
        return str(self)
    def buckets_str(self):
        output = ""
        for i, bucket in enumerate(self.buckets):
            pairs = [f"{k}:{v}" for k, v in bucket]
            output += f"{str(i).zfill(4)}->" + ", ".join(pairs) + "\n"
        return output
ht = Hashtable(5)
ht.put("apple", 10)
ht.put("banana", 20)
ht.put("apple", 5)
print("Hashtable:", ht)
print("Buckets:")
print(ht.buckets_str())
print("Get 'apple':", ht.get("apple"))
print("Get 'banana':", ht.get("banana"))
print("Get 'orange':", ht.get("orange"))