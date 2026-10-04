from htable import *
def fonk1():
    b1 = htable(5)
    assert htable_str(b1) == "{}"
    assert htable_buckets_str(b1) == (
        "0000->\n"
        "0001->\n"
        "0002->\n"
        "0003->\n"
        "0004->\n"
    )
def fonk2():
    b1 = htable(5)
    htable_put(b1, "parrt", 99)
    assert htable_str(b1) == "{parrt:99}"
    assert htable_buckets_str(b1) == (
        "0000->\n"
        "0001->\n"
        "0002->\n"
        "0003->parrt:99\n"
        "0004->\n"
    )
def fonk3():
    b1 = htable(5)
    htable_put(b1, "parrt", set([99]))
    assert htable_str(b1) == "{parrt:set([99])}"
    assert htable_buckets_str(b1) == (
        "0000->\n"
        "0001->\n"
        "0002->\n"
        "0003->parrt:set([99])\n"
        "0004->\n"
    )
def fonk4():
    b1 = htable(5)
    for i in range(1, 11):
        htable_put(b1, i, i)
    b2 = htable_str(b1)
    assert b2 = = "{5:5, 10:10, 1:1, 6:6, 2:2, 7:7, 3:3, 8:8, 4:4, 9:9}"
    b2 = htable_buckets_str(b1)
    assert b2 = = (
        "0000->5:5, 10:10\n"
        "0001->1:1, 6:6\n"
        "0002->2:2, 7:7\n"
        "0003->3:3, 8:8\n"
        "0004->4:4, 9:9\n"
    )
def fonk5():
    b1 = htable(5)
    htable_put(b1, "a", "x")
    htable_put(b1, "b", "y")
    htable_put(b1, "c", "z")
    htable_put(b1, "f", "i")
    htable_put(b1, "g", "j")
    htable_put(b1, "k", "k")
    b2 = htable_str(b1)
    assert b2 = = '{a:x, f:i, k:k, b:y, g:j, c:z}', "found " + b2
    b2 = htable_buckets_str(b1)
    assert b2 = = (
        "0000->\n"
        "0001->\n"
        "0002->a:x, f:i, k:k\n"
        "0003->b:y, g:j\n"
        "0004->c:z\n"
    )
def fonk6():
    b1 = htable(5)
    htable_put(b1, "parrt", [2, 99, 3942])
    htable_put(b1, "tombu", [6, 3, 1024, 99, 102342])
    assert htable_str(b1) == "{tombu:[6, 3, 1024, 99, 102342], parrt:[2, 99, 3942]}"
    assert htable_buckets_str(b1) == (
        "0000->\n"
        "0001->tombu:[6, 3, 1024, 99, 102342]\n"
        "0002->\n"
        "0003->parrt:[2, 99, 3942]\n"
        "0004->\n"
    )