
def rabin_karp_algo(text, substring):
    n = len(text)
    m = len(substring)
    if m > n:
        return []
    q = 101
    d = 128
    h = pow(d, m-1) % q
    substring_hash = sum(ord(substring[i]) * pow(d, m-i-1) for i in range(m)) % q
    text_hash = sum(ord(text[i]) * pow(d, m-i-1) for i in range(m)) % q
    found = []
    for i in range(n - m + 1):
        if text_hash == substring_hash:
            if text[i:i+m] == substring:
                found.append(i)
                print(f"Substring found at index {i}")
        if i < n - m:
            text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if text_hash < 0:
                text_hash += q
    return found
if __name__ == "__main__":
    text = 'Get bit; set bit; clear bit; update bit'
    substring = 'bit'
    print("Occurrences of substring:", rabin_karp_algo(text, substring))