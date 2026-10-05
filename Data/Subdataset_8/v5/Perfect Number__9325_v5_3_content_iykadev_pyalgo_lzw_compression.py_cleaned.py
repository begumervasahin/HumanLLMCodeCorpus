def compress(uncompressed):
    dictionary = {chr(i): chr(i) for i in range(256)}
    result = []
    w = ""
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = len(dictionary)
            w = c
    if w:
        result.append(dictionary[w])
    return result
def decompress(compressed):
    from io import StringIO
    dictionary = {chr(i): chr(i) for i in range(256)}
    result = StringIO()
    w = compressed.pop(0)
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == len(dictionary):
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed symbol: %s' % k)
        result.write(entry)
        dictionary[len(dictionary)] = w + entry[0]
        w = entry
    return result.getvalue()
compressed = compress('ALIALIALIALIALI')
print("Compressed:", compressed)
decompressed = decompress(compressed)
print("Decompressed:", decompressed)