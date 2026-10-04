import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, words
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
import enchant
b1 = set(stopwords.words("english"))
b2 = WordNetLemmatizer()
b3 = enchant.Dict("en_US")
b4 = set(words.words())
with open('new_tweets.txt', 'r') as f, open("new_preprocessed.txt", "a") as output:
    for b5 in f:
        b5 = b5.split(',b5:')[1].strip()
        b6 = b5.lower()
        b6 = ''.join([char for char in b6 if not char.isdigit() and char not in string.punctuation])
        b7 = " ".join([word for word in b6.split() if not word.startswith('@') and len(word) > 2 and b3.check(word)])
        b8 = word_tokenize(b7)
        b9 = [word for word in b8 if word not in b1]
        b10 = [b2.lemmatize(word) for word in b9]
        b11 = nltk.pos_tag(b10)
        b12 = [word for word, tag in b11 if tag not in ('NNP', 'NNPS')]
        output.write(" ".join(b12) + "\n")