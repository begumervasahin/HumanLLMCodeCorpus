from htable_oo import HashTable
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
    assert str(table) == "{5:5, 10:10, 1:1, 6:6, 2:2, 7:7, 3:3, 8:8, 4:4, 9:9}"
    assert table.buckets_str() ==
def test_str_to_set():
    table = HashTable(5)
    table.put("parrt", {2, 99, 3942})
    table.put("tombu", {6, 3, 1024, 99, 102342})
    assert str(table) == "{tombu:{1024, 99, 3, 102342, 6}, parrt:{2, 99, 3942}}"
    assert table.buckets_str() ==