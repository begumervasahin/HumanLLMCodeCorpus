import re
from collections import Counter
def load_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()
    word_list = re.findall(r'\w+', text)
    return Counter(word_list)
def probability(word, total_words):
    return WORDS_DICT[word] / total_words
def correct(word):
    return max(candidates(word), key=lambda w: probability(w, total_words))
def candidates(word):
    return (known([word]) or
            known(edits1(word)) or
            known(edits2(word)) or
            {word})
def known(words):
    return {w for w in words if w in WORDS_DICT}
def edits1(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)
def edits2(word):
    return {e2 for e1 in edits1(word) for e2 in edits1(e1)}
if __name__ == '__main__':
    WORDS_DICT = load_words('LargeTextFile.txt')
    total_words = sum(WORDS_DICT.values())
    test_word = 'speling'
    print(f'Corrected word: {correct(test_word)}')