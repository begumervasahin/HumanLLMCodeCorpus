import nltk
import warnings
import numpy as np
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
warnings.filterwarnings("ignore")
with open('nlp_python_answer_finals.txt', 'r', b1 = 'ignore') as f:
    b2 = f.read().lower()
with open('modules_pythons.txt', 'r', b1 = 'ignore') as m:
    b3 = m.read().lower()
b4 = nltk.sent_tokenize(b2)
b5 = nltk.word_tokenize(b2)
b6 = nltk.sent_tokenize(b3)
b7 = nltk.word_tokenize(b3)
b8 = nltk.stem.WordNetLemmatizer()
def fonk1(tokens):
    return [b8.lemmatize(token) for token in tokens]
b9 = dict((ord(punct), None) for punct in string.punctuation)
def fonk2(text):
    return fonk1(nltk.word_tokenize(text.lower().translate(b9)))
b10 = ["My name is PyBot.", "My name is PyBot you can call me Pi.",
                 "I'm PyBot :)", "My name is PyBot and my nickname is Pi. I am happy to solve your queries :)"]
b11 = ("hello", "hi", "hey", "greetings", "sup", "what's up")
b12 = ["Hi", "Hey", "Hello", "I am glad you are talking to me"]
b13 = ("what is python ?", "what is python")
b14 = ("Python is a high-level, interpreted, interactive and object-oriented scripting programming language. "
             "Python is designed to be highly readable. It uses English keywords frequently whereas other languages "
             "use punctuation, and it has fewer syntactical constructions than other languages.")
b15 = ("what is module", "what is module?")
b16 = ["Consider a module to be the same as a code library.",
                    "A file containing a set of functions you want to include in your application.",
                    "A module can define functions, classes and variables. A module can also include runnable code. "
                    "Grouping related code into a module makes the code easier to understand and use."]
def fonk3(sentence):
    for word in sentence.split():
        if word.lower() in b11:
            return random.choice(b12)
def fonk4(sentence):
    for word in b13:
        if sentence.lower() == word:
            return b14
def fonk5(sentence):
    for word in b15:
        if sentence.lower() == word:
            return random.choice(b16)
def fonk6(sentence):
    return random.choice(b10)
def fonk7(b24, b4):
    b17 = ''
    b4.append(b24)
    b18 = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    b19 = b18.fit_transform(b4)
    b20 = cosine_similarity(b19[-1], b19)
    b21 = b20.argsort()[0][-2]
    b22 = b20.flatten()
    b22.sort()
    b23 = b22[-2]
    if b23 = = 0:
        b17 = "I am sorry! I don't understand you"
    else:
        b17 = b4[b21]
    return b17
def fonk8(b24):
    b24 = b24.lower()
    b25 = "module"
    if b24 != 'bye':
        if b24 = = 'thanks' or b24 == 'thank you':
            return "You are welcome.."
        elif fonk5(b24) is not None:
            return fonk5(b24)
        else:
            if b25 in b24:
                return fonk7(b24, b6)
            elif fonk3(b24) is not None:
                return fonk3(b24)
            elif "your name" in b24:
                return fonk6(b24)
            elif fonk4(b24) is not None:
                return fonk4(b24)
            else:
                return fonk7(b24, b4)
    else:
        return "Bye! take care.."
if b26 = = "__main__":
    nltk.download('punkt')
    nltk.download('wordnet')
    while True:
        b27 = input("You: ")
        b28 = fonk8(b27)
        print("PyBot:", b28)
        if b27.lower() == 'bye':
            break