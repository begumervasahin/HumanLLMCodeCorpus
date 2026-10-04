from itertools import combinations
def strxor(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))
def list_of_words(of_length: int) -> list:
    dummy_words = ['hello', 'world', 'apple', 'lemon', 'peach']
    return [word.encode('utf-8') for word in dummy_words if len(word) == of_length]
def main() -> None:
    c1 = b'\x0b\x0e\x1e\x0b\x17'
    c2 = b'\x15\x0a\x1b\x1d\x01'
    words = list_of_words(of_length=len(c1))
    pairs = combinations(words, 2)
    for word1, word2 in pairs:
        xor_result = strxor(word1, word2)
        print(f'Word 1: {word1.decode("utf-8")}, Word 2: {word2.decode("utf-8")}, XOR Result: {xor_result}')
if __name__ == "__main__":
    main()