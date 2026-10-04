import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import enchant
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
b1 = set(stopwords.words("english"))
b2 = enchant.Dict("en_US")
b3 = set(nltk.corpus.words.words())
b4 = WordNetLemmatizer()
b5 = open("new_preprocessed.txt", "a")
with open('new_tweets.txt', 'r') as f:
    for b6 in f:
        b6 = b6.split(',b6:')[1]
        b7 = b6.lower()
        b7 = ''.join([i for i in b7 if not i.isdigit() and i not in string.punctuation])
        b8 = ""
        for word in b7.split(' '):
            if not word.startswith('@') and len(word) > 2 and b2.check(word):
                b8 += " " + word
        b9 = word_tokenize(b8)
        b10 = [w for w in b9 if w not in b1]
        b11 = [b4.lemmatize(word) for word in b10]
        b12 = nltk.pos_tag(b11)
        b13 = [word for word, tag in b12 if tag != 'NNP' and tag != 'NNPS']
        b5.write(" ".join(b13))
        b5.write("\n")
b5.close()