def make_vernam_cipher(text, key):
    answer = ""
    p = 0
    for char in text:
        answer += chr(ord(char) ^ ord(key[p]))
        p += 1
        if p == len(key):
            p = 0
    return answer
MY_KEY = "cvwopslweinedvq9fnasdlkfn2"
if __name__ == "__main__":
    while True:
        print("\n\n--- Vernam Cipher ---")
        plaintext = input("Enter text to encrypt: ")
        cipher = make_vernam_cipher(plaintext, MY_KEY)
        print("Cipher text: " + cipher)
        decrypted_text = make_vernam_cipher(cipher, MY_KEY)
        print("Decrypted text: " + decrypted_text)