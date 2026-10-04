from cp_otp import strxor
from cp_dictionary import list_of_words
from itertools import combinations
def generate_word_pairs(word_length):
    words = list_of_words(of_length=word_length)
    return list(combinations(words, r=2))
def main():
    c1 = b'\x0b\x0e\x1e\x0b\x17'
    c2 = b'\x15\x0a\x1b\x1d\x01'
    word_length = len(c1)
    pairs = generate_word_pairs(word_length)
    for pair in pairs:
        print(pair)
if __name__ == "__main__":
    main()