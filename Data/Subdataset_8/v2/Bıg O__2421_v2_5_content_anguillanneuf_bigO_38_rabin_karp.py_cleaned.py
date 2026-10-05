def rabin_karp_search(text, substring):
    found_indices = []
    text_length = len(text)
    substring_length = len(substring)
    prime = 101
    d = 128
    h = pow(d, substring_length - 1) % prime
    def hash_function(s):
        hash_val = 0
        for char in s:
            hash_val = (hash_val * d + ord(char)) % prime
        return hash_val
    substring_hash = hash_function(substring)
    text_hash = hash_function(text[:substring_length])
    for i in range(text_length - substring_length + 1):
        if substring_hash == text_hash:
            if text[i:i+substring_length] == substring:
                found_indices.append(i)
                print("Substring found at index:", i)
        if i < text_length - substring_length:
            text_hash = (d * (text_hash - h * ord(text[i])) + ord(text[i + substring_length])) % prime
            if text_hash < 0:
                text_hash += prime
    return found_indices
text = 'Get bit; set bit; clear bit; update bit'
substring = 'bit'
print("Indices of substring found using Rabin-Karp algorithm:", rabin_karp_search(text, substring))