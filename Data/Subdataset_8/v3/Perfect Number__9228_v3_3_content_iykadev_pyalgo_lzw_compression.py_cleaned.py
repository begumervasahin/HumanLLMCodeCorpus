def compress_string(uncompressed):
    dictionary_size = 256
    dictionary = {chr(i): chr(i) for i in range(dictionary_size)}
    compressed_result = []
    current_string = ""
    for char in uncompressed:
        new_string = current_string + char
        if new_string in dictionary:
            current_string = new_string
        else:
            compressed_result.append(dictionary[current_string])
            dictionary[new_string] = dictionary_size
            dictionary_size += 1
            current_string = char
    if current_string:
        compressed_result.append(dictionary[current_string])
    return compressed_result
def decompress_string(compressed):
    dictionary_size = 256
    dictionary = {chr(i): chr(i) for i in range(dictionary_size)}
    decompressed_result = []
    current_string = compressed.pop(0)
    decompressed_result.append(current_string)
    for code in compressed:
        if code in dictionary:
            entry = dictionary[code]
        elif code == dictionary_size:
            entry = current_string + current_string[0]
        else:
            raise ValueError('Bad compressed code: %s' % code)
        decompressed_result.append(entry)
        dictionary[dictionary_size] = current_string + entry[0]
        dictionary_size += 1
        current_string = entry
    return ''.join(decompressed_result)
compressed = compress_string('ALIALIALIALIALI')
print("Compressed:", compressed)
decompressed = decompress_string(compressed)
print("Decompressed:", decompressed)