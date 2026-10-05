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
with open("new_preprocessed.txt", "a") as output_file:
    with open('new_tweets.txt', 'r') as input_file:
        for line in input_file:
            b3 = line.split(',text:')[1]
            b4 = fonk1(b3)
            b5 = word_tokenize(b4)
            b6 = fonk3(b5)
            b7 = fonk4(b6)
            b8 = fonk5(b7)
            output_file.write(" ".join(b8) + "\n")
def fonk1(b3):
    b9 = b3.lower()
    b4 = ''.join([char for char in b9 if not char.isdigit() and char not in string.punctuation])
    b10 = " ".join(word for word in b4.split() if fonk2(word))
    return b10
def fonk2(word):
    return not word.startswith('@') and len(word) > 2 and b1.check(word)
def fonk3(words):
    return [word for word in words if word not in b2]
def fonk4(words):
    b11 = WordNetLemmatizer()
    return [b11.lemmatize(word) for word in words]
def fonk5(words):
    b12 = nltk.tag.pos_tag(words)
    return [word for word, tag in b12 if tag != 'NNP' and tag != 'NNPS']