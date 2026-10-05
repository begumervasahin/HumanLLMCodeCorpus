
def create_hashtable(nbuckets):
    return [[] for _ in range(nbuckets)]
def generate_hashcode(o):
    if isinstance(o, int):
        return o
    elif isinstance(o, str):
        h = 0
        for char in o:
            h = h * 31 + ord(char)
        return h
    else:
        return None
def insert_entry(table, key, value):
    if table is None or len(table) == 0:
        return
    bucket_index = generate_hashcode(key) % len(table)
    bucket = table[bucket_index]
    for i, (existing_key, existing_value) in enumerate(bucket):
        if existing_key == key:
            bucket[i] = (key, existing_value | value)
            return
    bucket.append((key, value))
def get_value(table, key):
    if table is None or len(table) == 0:
        return None
    bucket_index = generate_hashcode(key) % len(table)
    bucket = table[bucket_index]
    for entry_key, entry_value in bucket:
        if entry_key == key:
            return entry_value
    return None
def hashtable_buckets_str(table):
    if table is None:
        return None
    output = ""
    for i, bucket in enumerate(table):
        output += str(i).zfill(4) + '->'
        for entry_key, entry_value in bucket:
            output += str(entry_key) + ':' + str(entry_value) + ', '
        output = output.rstrip(', ') + '\n'
    return output
def hashtable_str(table):
    if table is None:
        return None
    output = '{'
    for bucket in table:
        for entry_key, entry_value in bucket:
            output += str(entry_key) + ':' + str(entry_value) + ', '
    output = output.rstrip(', ') + '}'
    return output