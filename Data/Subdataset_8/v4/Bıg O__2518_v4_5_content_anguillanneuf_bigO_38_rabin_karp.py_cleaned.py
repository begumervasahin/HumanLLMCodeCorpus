def rabin_karp_search(text, substring):
    found_indices = []
    text_length = len(text)
    substring_length = len(substring)
    prime = 101
    d = 128
    h = 1
    for i in range(substring_length - 1):
        h = (h * d) % prime
    substring_hash = 0
    text_hash = 0
    for i in range(substring_length):
        substring_hash = (d * substring_hash + ord(substring[i])) % prime
        text_hash = (d * text_hash + ord(text[i])) % prime
    for i in range(text_length - substring_length + 1):
        if substring_hash == text_hash:
            if text[i:i + substring_length] == substring:
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