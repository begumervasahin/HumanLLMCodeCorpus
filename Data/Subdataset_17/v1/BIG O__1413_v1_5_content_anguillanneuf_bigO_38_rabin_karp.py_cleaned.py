
def rabin_karp_algo(text, substring):
    found = []
    n = len(text)
    m = len(substring)
    q = 101
    d = 128
    h = 1
    for i in range(m-1):
        h = (h * d) % q
    substring_hash = 0
    text_hash = 0
    for i in range(m):
        substring_hash = (d * substring_hash + ord(substring[i])) % q
        text_hash = (d * text_hash + ord(text[i])) % q
    for i in range(n - m + 1):
        if substring_hash == text_hash:
            match = True
            for j in range(m):
                if text[i + j] != substring[j]:
                    match = False
                    break
            if match:
                found.append(i)
                print(f"Substring found at index {i}")
        if i < n - m:
            text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if text_hash < 0:
                text_hash += q
    return found
print(rabin_karp_algo('Get bit; set bit; clear bit; update bit', 'bit'))