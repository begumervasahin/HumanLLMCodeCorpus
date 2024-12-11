from htable_oo import HashTable
def fonk1():
    b1 = HashTable(5)
    assert str(b1) == "{}"
    assert b1.buckets_str() ==
def fonk2():
    b1 = HashTable(5)
    b1.put("parrt", 99)
    assert str(b1) == "{parrt:99}"
    assert b1.buckets_str() ==
def fonk3():
    b1 = HashTable(5)
    for i in range(1, 11):
        b1.put(i, i)
    assert str(b1) == "{5:5, 10:10, 1:1, 6:6, 2:2, 7:7, 3:3, 8:8, 4:4, 9:9}"
    assert b1.buckets_str() ==
def fonk4():
    b1 = HashTable(5)
    b1.put("parrt", {2, 99, 3942})
    b1.put("tombu", {6, 3, 1024, 99, 102342})
    assert str(b1) == "{tombu:{1024, 99, 3, 102342, 6}, parrt:{2, 99, 3942}}"
    assert b1.buckets_str() ==