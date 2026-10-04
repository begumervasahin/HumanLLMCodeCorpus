from htable import *
def test_empty_hash_table():
    table = htable(5)
    assert htable_str(table) == "{}"
    assert htable_buckets_str(table) ==
def test_single_key_value_pair():
    table = htable(5)
    htable_put(table, "parrt", 99)
    assert htable_str(table) == "{parrt:99}"
    assert htable_buckets_str(table) ==
def test_single_key_set_pair():
    table = htable(5)
    htable_put(table, "parrt", set([99]))
    assert htable_str(table) == "{parrt:set([99])}"
    assert htable_buckets_str(table) ==
def test_int_keys_and_values():
    table = htable(5)
    for i in range(1, 11):
        htable_put(table, i, i)
    assert htable_str(table) == "{5:5, 10:10, 1:1, 6:6, 2:2, 7:7, 3:3, 8:8, 4:4, 9:9}"
    assert htable_buckets_str(table) ==
def test_string_keys_and_values():
    table = htable(5)
    htable_put(table, "a", "x")
    htable_put(table, "b", "y")
    htable_put(table, "c", "z")
    htable_put(table, "f", "i")
    htable_put(table, "g", "j")
    htable_put(table, "k", "k")
    assert htable_str(table) == '{a:x, f:i, k:k, b:y, g:j, c:z}'
    assert htable_buckets_str(table) ==
def test_string_keys_and_list_values():
    table = htable(5)
    htable_put(table, "parrt", [2, 99, 3942])
    htable_put(table, "tombu", [6, 3, 1024, 99, 102342])
    assert htable_str(table) == "{tombu:[6, 3, 1024, 99, 102342], parrt:[2, 99, 3942]}"
    assert htable_buckets_str(table) ==
if __name__ == "__main__":
    test_empty_hash_table()
    test_single_key_value_pair()
    test_single_key_set_pair()
    test_int_keys_and_values()
    test_string_keys_and_values()
    test_string_keys_and_list_values()
    print("All tests passed!")