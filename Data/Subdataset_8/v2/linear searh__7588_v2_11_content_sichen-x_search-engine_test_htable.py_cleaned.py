class HashTable:
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(size)]
    def __str__(self):
        items = []
        for bucket in self.buckets:
            for key, value in bucket:
                items.append(f"{key}:{value}")
        return "{" + ", ".join(items) + "}"
    def put(self, key, value):
        index = hash(key) % self.size
        bucket = self.buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
    def __getitem__(self, key):
        index = hash(key) % self.size
        for k, v in self.buckets[index]:
            if k == key:
                return v
        raise KeyError(key)
    def __setitem__(self, key, value):
        self.put(key, value)
    def bucket_str(self):
        result = ""
        for i, bucket in enumerate(self.buckets):
            result += f"{str(i).zfill(4)}->"
            if bucket:
                result += ", ".join(f"{k}:{v}" for k, v in bucket)
            result += "\n"
        return result
def test_empty():
    table = HashTable(5)
    assert str(table) == "{}"
    assert table.bucket_str() ==
def test_single():
    table = HashTable(5)
    table["parrt"] = 99
    assert str(table) == "{parrt:99}"
    assert table.bucket_str() ==
def test_singleon():
    table = HashTable(5)
    table["parrt"] = set([99])
    assert str(table) == "{parrt:{99}}"
    assert table.bucket_str() ==
def test_int_to_int():
    table = HashTable(5)
    for i in range(1, 11):
        table[i] = i
    s = str(table)
    assert s == "{1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10}"
    s = table.bucket_str()
    assert s ==
def test_str_to_str():
    table = HashTable(5)
    table["a"] = "x"
    table["b"] = "y"
    table["c"] = "z"
    table["f"] = "i"
    table["g"] = "j"
    table["k"] = "k"
    s = str(table)
    assert s == "{a:x, b:y, c:z, f:i, g:j, k:k}"
    s = table.bucket_str()
    assert s ==
def test_str_to_set():
    table = HashTable(5)
    table["parrt"] = [2, 99, 3942]
    table["tombu"] = [6, 3, 1024, 99, 102342]
    assert str(table) == "{parrt:[2, 99, 3942], tombu:[6, 3, 1024, 99, 102342]}"
    assert table.bucket_str() ==
if __name__ == "__main__":
    test_empty()
    test_single()
    test_singleon()
    test_int_to_int()
    test_str_to_str()
    test_str_to_set()
    print("All tests passed!")