import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import enchant
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
b1 = enchant.Dict("en_US")
b2 = set(stopwords.words("english"))
b3 = open("new_preprocessed.txt", "a")
with open('new_tweets.txt', 'r') as input_file:
    for line in input_file:
        b4 = line.split(',b4:')[1]
        b5 = b4.lower()
        b5 = ''.join([i for i in b5 if not i.isdigit() and i not in string.punctuation])
        b6 = ""
        for word in b5.split(' '):
            if (not word.startswith('@') and len(word) > 2 and b1.check(word)):
                b6 += " " + word
        b7 = word_tokenize(b6)
        b8 = [w for w in b7 if w not in b2]
        b9 = WordNetLemmatizer()
        b10 = [b9.lemmatize(word) for word in b8]
        b11 = nltk.tag.pos_tag(b10)
        b12 = [word for word, tag in b11 if tag != 'NNP' and tag != 'NNPS']
        b3.write(" ".join(b12) + "\n")
b3.close()