def vernam(key, text):
    answer = ""
    p = 0
    for char in text:
        answer += chr(ord(char) ^ ord(key[p]))
        p += 1
        if p == len(key):
            p = 0
    return answer
def main():
    key = "SECRET"
    text = "HELLO WORLD"
    encrypted = vernam(key, text)
    print("Encrypted:", encrypted)
    decrypted = vernam(key, encrypted)
    print("Decrypted:", decrypted)
if __name__ == "__main__":
    main()