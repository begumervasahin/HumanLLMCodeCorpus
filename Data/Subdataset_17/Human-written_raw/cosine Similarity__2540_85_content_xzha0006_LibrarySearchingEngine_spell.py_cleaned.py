import re
from collections import Counter
word_list = re.findall(r'\w+', open('LargeTextFile.txt').read().lower())
WORDS_DICT = Counter(word_list)
def probability(word, N=sum(WORDS_DICT.values())):
    return WORDS_DICT[word] / N
def correct(word):
    return max(candidates(word), key=probability)
def candidates(word):
    if len(known([word])) != 0:
        return known([word])
    elif len(known(levenshtein(word))) != 0:
        return known(levenshtein(word))
    elif len(known(levenshtein2(word))) != 0:
        return known(levenshtein2(word))
    else:
        return [word]
def known(words):
    return set(w for w in words if w in WORDS_DICT)
def levenshtein(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletion = [Left + Right[1:] for Left, Right in splits if Right]
    transposition = [Left + Right[1] + Right[0] + Right[2:] for Left, Right in splits if len(Right)>1]
    replacement = [Left + char + Right[1:] for Left, Right in splits if Right for char in letters]
    insertion = [Left + char + Right for Left, Right in splits for char in letters]
    return set(deletion + transposition + replacement + insertion)
def levenshtein2(word):
    return (j for i in levenshtein(word) for j in levenshtein(i))