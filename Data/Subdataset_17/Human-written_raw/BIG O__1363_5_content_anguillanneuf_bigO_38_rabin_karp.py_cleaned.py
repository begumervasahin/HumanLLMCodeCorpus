
def rabin_karp_algo(text, substring):
    found = []
    n = len(text)
    m = len(substring)
    q = 101
    d = 128
    h = d**(m-1)%q
    h = 1
    for i in range(m-1):
        h = h*d % q
    substring_hash = 0
    text_hash = 0
    for i in range(m):
        substring_hash = ( d*(substring_hash - h*0) + ord(substring[i]) ) % q
        text_hash      = ( d*(text_hash - h*0)      + ord(text[i])      ) % q
    for i in range(n-m+1):
        if substring_hash == text_hash:
            for j in range(m):
                if text[i+j]!=substring[j]:
                    break
            else:
                found.append(i)
                print("Substring found at {}".format(i))
        if i < n - m:
            text_hash = ( d*(text_hash - h*ord(text[i])) + ord(text[i+m]) ) % q
            if text_hash < 0:
                text_hash += q
    return found
print(rabin_karp_algo('Get bit; set bit; clear bit; update bit', 'bit'))