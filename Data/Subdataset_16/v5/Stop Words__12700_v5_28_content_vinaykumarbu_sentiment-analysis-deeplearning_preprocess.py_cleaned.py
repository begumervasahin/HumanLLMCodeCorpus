import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, words
from nltk.stem import WordNetLemmatizer
import enchant
b1 = set(stopwords.words("english"))
b2 = WordNetLemmatizer()
b3 = enchant.Dict("en_US")
b4 = set(words.words())
def fonk1(b5):
    b5 = b5.split(',b5:')[1].strip().lower()
    b5 = ''.join([char for char in b5 if not char.isdigit() and char not in string.punctuation])
    b6 = [word for word in b5.split() if not word.startswith('@') and len(word) > 2 and b3.check(word)]
    b7 = word_tokenize(" ".join(b6))
    b8 = [word for word in b7 if word not in b1]
    b9 = [b2.lemmatize(word) for word in b8]
    b10 = nltk.pos_tag(b9)
    b11 = [word for word, tag in b10 if tag not in ('NNP', 'NNPS')]
    return b11
def fonk2():
    b12 = 'new_tweets.txt'
    b13 = 'new_preprocessed.txt'
    with open(b12, 'r') as f, open(b13, 'a') as output:
        for b5 in f:
            b14 = fonk1(b5)
            output.write(" ".join(b14) + "\n")
if b15 = = "__main__":
    fonk2()