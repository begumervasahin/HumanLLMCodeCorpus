class Hashtable:
    def __init__(self, nbuckets):
        self.buckets = [[] for _ in range(nbuckets)]
    def _hash(self, key):
        if isinstance(key, int):
            return key
        if isinstance(key, str):
            return sum(31 ** i * ord(char) for i, char in enumerate(key))
        raise TypeError("Unsupported key type")
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
        pairs = (f"{k}:{v}" for bucket in self.buckets for k, v in bucket)
        return "{" + ", ".join(pairs) + "}"
    def __repr__(self):
        return self.__str__()
    def buckets_str(self):
        output = []
        for i, bucket in enumerate(self.buckets):
            pairs = ", ".join(f"{k}:{v}" for k, v in bucket)
            output.append(f"{str(i).zfill(4)}-> {pairs}")
        return "\n".join(output)
if __name__ == "__main__":
    ht = Hashtable(5)
    ht.put("apple", 10)
    ht.put("banana", 20)
    ht.put("apple", 5)
    print("Hashtable:", ht)
    print("Buckets:", ht.buckets_str())
    print("Get 'apple':", ht.get("apple"))
    print("Get 'banana':", ht.get("banana"))
    print("Get 'orange':", ht.get("orange"))