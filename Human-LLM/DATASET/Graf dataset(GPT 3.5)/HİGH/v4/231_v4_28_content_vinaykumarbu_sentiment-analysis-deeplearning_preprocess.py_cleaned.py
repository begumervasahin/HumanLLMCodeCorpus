import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import enchant
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
b1 = set(stopwords.words("english"))
b2 = enchant.Dict("en_US")
b3 = open('new_tweets.txt', 'r')
b4 = open("new_preprocessed.txt", "a")
for line in b3:
    b5 = line.split(',b5:')[1]
    b6 = ''.join([char for char in b5.lower() if not char.isdigit() and char not in string.punctuation])
    b7 = ""
    for word in b6.split():
        if not word.startswith('@') and len(word) > 2 and b2.check(word):
            b7 += " " + word
    b8 = word_tokenize(b7)
    b9 = [word for word in b8 if word not in b1]
    b10 = WordNetLemmatizer()
    b11 = [b10.lemmatize(word) for word in b9]
    b12 = nltk.tag.pos_tag(b11)
    b13 = [word for word, tag in b12 if tag != 'NNP' and tag != 'NNPS']
    b4.write(" ".join(b13))
    b4.write("\n")
b3.close()
b4.close()