
def htable(nbuckets):
    the_table = []
    for i in range(nbuckets):
        the_table.append([])
    return the_table
def hashcode(o):
    if isinstance(o, int):
        return o
    elif isinstance(o, str):
        h = 0
        for char in o:
            h = h * 31 + ord(char)
        return h
    else:
        return None
def htable_put(table, key, value):
    if table is None or len(table) == 0:
        return
    bucket_index = hashcode(key) % len(table)
    bucket = table[bucket_index]
    for i in range(len(bucket)):
        if bucket[i][0] == key:
            new_value = bucket[i][1] | value
            bucket[i] = (key, new_value)
            return
    bucket.append((key, value))
def htable_get(table, key):
    if table is None or len(table) == 0:
        return None
    bucket_index = hashcode(key) % len(table)
    bucket = table[bucket_index]
    for node in bucket:
        if node[0] == key:
            return node[1]
    return None
def htable_buckets_str(table):
    if table is None:
        return None
    output = ""
    for i in range(len(table)):
        output += str(i).zfill(4) + '->'
        for node in table[i]:
            output += str(node[0]) + ':' + str(node[1]) + ', '
        output = output.rstrip(', ') + '\n'
    return output
def htable_str(table):
    if table is None:
        return None
    output = '{'
    for i in range(len(table)):
        for node in table[i]:
            output += str(node[0]) + ':' + str(node[1]) + ', '
    output = output.rstrip(', ') + '}'
    return output