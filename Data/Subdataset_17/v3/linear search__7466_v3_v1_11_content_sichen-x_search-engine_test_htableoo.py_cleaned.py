class HashTable:
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(size)]
    def __str__(self):
        pairs = [
            f"{key}:{value}"
            for bucket in self.buckets
            for key, value in bucket
        ]
        return "{" + ", ".join(pairs) + "}"
    def buckets_str(self):
        result = ""
        for i, bucket in enumerate(self.buckets):
            result += f"{str(i).zfill(4)}->"
            if bucket:
                pairs = ", ".join([f"{key}:{value}" for key, value in bucket])
                result += pairs
            result += "\n"
        return result
    def hash_function(self, key):
        return hash(key) % self.size
    def put(self, key, value):
        index = self.hash_function(key)
        for i, (existing_key, _) in enumerate(self.buckets[index]):
            if existing_key == key:
                self.buckets[index][i] = (key, value)
                return
        self.buckets[index].append((key, value))
def test_empty():
    table = HashTable(5)
    assert str(table) == "{}"
    assert table.buckets_str() ==
def test_single():
    table = HashTable(5)
    table.put("parrt", 99)
    assert str(table) == "{parrt:99}"
    assert table.buckets_str() ==
def test_a_few():
    table = HashTable(5)
    for i in range(1, 11):
        table.put(i, i)
    s = str(table)
    assert s == "{5:5, 10:10, 1:1, 6:6, 2:2, 7:7, 3:3, 8:8, 4:4, 9:9}"
    s = table.buckets_str()
    assert s ==
def test_str_to_set():
    table = HashTable(5)
    table.put("parrt", {2, 99, 3942})
    table.put("tombu", {6, 3, 1024, 99, 102342})
    assert str(table) == "{tombu:{1024, 99, 3, 102342, 6}, parrt:{2, 99, 3942}}"
    assert table.buckets_str() ==
if __name__ == "__main__":
    test_empty()
    test_single()
    test_a_few()
    test_str_to_set()
    print("All tests passed!")