import string
import nltk
import enchant
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
b1 = set(stopwords.words("english"))
b2 = enchant.Dict("en_US")
b3 = WordNetLemmatizer()
def fonk1(b4):
    b4 = b4.lower()
    b4 = ''.join(char for char in b4 if not char.isdigit() and char not in string.punctuation)
    b5 = " ".join(
        word for word in b4.split()
        if not word.startswith('@') and len(word) > 2 and b2.check(word)
    )
    b6 = word_tokenize(b5)
    b7 = [word for word in b6 if word not in b1]
    b8 = [b3.lemmatize(word) for word in b7]
    b9 = nltk.pos_tag(b8)
    b10 = [word for word, tag in b9 if tag not in ('NNP', 'NNPS')]
    return " ".join(b10)
def fonk2(input_file_path, output_file_path):
    with open(output_file_path, "a") as output_file:
        with open(input_file_path, 'r') as input_file:
            for line in input_file:
                try:
                    b11 = line.split(',text:')[1]
                    b12 = fonk1(b11)
                    output_file.write(b12 + "\n")
                except IndexError:
                    continue
fonk2('new_tweets.txt', 'new_preprocessed.txt')