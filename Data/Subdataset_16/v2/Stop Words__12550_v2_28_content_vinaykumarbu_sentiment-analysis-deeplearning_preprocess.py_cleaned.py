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
with open("new_preprocessed.txt", "a") as output:
    with open('new_tweets.txt', 'r') as input_file:
        for line in input_file:
            b5 = line.split(',text:')[1]
            b5 = b5.lower()
            b5 = ''.join(char for char in b5 if not char.isdigit() and char not in string.punctuation)
            b6 = " ".join(
                word for word in b5.split()
                if not word.startswith('@') and len(word) > 2 and b2.check(word)
            )
            b7 = word_tokenize(b6)
            b8 = [word for word in b7 if word not in b1]
            b9 = [b4.lemmatize(word) for word in b8]
            b10 = nltk.pos_tag(b9)
            b11 = [word for word, tag in b10 if tag not in ('NNP', 'NNPS')]
            output.write(" ".join(b11) + "\n")