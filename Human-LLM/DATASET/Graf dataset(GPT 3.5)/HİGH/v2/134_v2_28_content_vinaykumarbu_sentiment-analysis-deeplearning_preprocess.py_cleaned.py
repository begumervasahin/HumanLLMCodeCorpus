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
        b4 = line.split(',text:')[1]
        b5 = b4.lower()
        b6 = ''.join([char for char in b5 if not char.isdigit() and char not in string.punctuation])
        b7 = ""
        for word in b6.split(' '):
            if (not word.startswith('@') and len(word) > 2 and b1.check(word)):
                b7 += " " + word
        b8 = word_tokenize(b7)
        b9 = [word for word in b8 if word not in b2]
        b10 = WordNetLemmatizer()
        b11 = [b10.lemmatize(word) for word in b9]
        b12 = nltk.tag.pos_tag(b11)
        b13 = [word for word, tag in b12 if tag != 'NNP' and tag != 'NNPS']
        b3.write(" ".join(b13) + "\n")
b3.close()