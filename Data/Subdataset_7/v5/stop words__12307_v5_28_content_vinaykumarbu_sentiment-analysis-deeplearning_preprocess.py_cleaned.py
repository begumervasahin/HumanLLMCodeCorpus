import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import enchant
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
b1 = set(stopwords.words("english"))
b2 = enchant.Dict("en_US")
with open('new_tweets.txt', 'r') as input_file, open("new_preprocessed.txt", "a") as output_file:
    for line in input_file:
        b3 = line.split(',b3:')[1]
        b4 = ''.join([char.lower() for char in b3 if not char.isdigit() and char not in string.punctuation])
        b5 = " ".join(word for word in b4.split() if not word.startswith('@') and len(word) > 2 and b2.check(word))
        b6 = word_tokenize(b5)
        b7 = [word for word in b6 if word not in b1]
        b8 = WordNetLemmatizer()
        b9 = [b8.lemmatize(word) for word in b7]
        b10 = nltk.tag.pos_tag(b9)
        b11 = [word for word, tag in b10 if tag not in ('NNP', 'NNPS')]
        output_file.write(" ".join(b11))
        output_file.write("\n")