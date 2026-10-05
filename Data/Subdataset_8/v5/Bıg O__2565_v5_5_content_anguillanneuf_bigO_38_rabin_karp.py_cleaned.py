def rabin_karp_search(text, substring):
    found_indices = []
    prime = 101
    character_set_size = 128
    text_length = len(text)
    substring_length = len(substring)
    h = pow(character_set_size, substring_length - 1) % prime
    substring_hash = calculate_hash(substring, prime, character_set_size)
    text_hash = calculate_hash(text[:substring_length], prime, character_set_size)
    for i in range(text_length - substring_length + 1):
        if substring_hash == text_hash:
            if text[i:i + substring_length] == substring:
                found_indices.append(i)
                print("Substring found at index:", i)
        if i < text_length - substring_length:
            text_hash = update_hash(text_hash, text[i], text[i + substring_length], h, prime, character_set_size)
    return found_indices
def calculate_hash(string, prime, character_set_size):
    hash_value = 0
    for char in string:
        hash_value = (hash_value * character_set_size + ord(char)) % prime
    return hash_value
def update_hash(old_hash, old_char, new_char, h, prime, character_set_size):
    new_hash = (old_hash - ord(old_char) * h) % prime
    new_hash = (new_hash * character_set_size + ord(new_char)) % prime
    return new_hash if new_hash >= 0 else new_hash + prime
text = 'Get bit; set bit; clear bit; update bit'
substring = 'bit'
print("Indices of substring found using Rabin-Karp algorithm:", rabin_karp_search(text, substring))