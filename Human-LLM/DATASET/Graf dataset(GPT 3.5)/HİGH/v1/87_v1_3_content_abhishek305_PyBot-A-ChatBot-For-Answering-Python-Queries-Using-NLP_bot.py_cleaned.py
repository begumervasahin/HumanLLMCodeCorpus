import nltk
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
b1 = open('nlp_python_answer_finals.txt', 'r', errors='ignore')
b2 = open('modules_pythons.txt', 'r', errors='ignore')
b3 = b1.read().lower()
b4 = b2.read().lower()
b5 = nltk.sent_tokenize(b3)
b6 = nltk.sent_tokenize(b4)
b7 = nltk.stem.WordNetLemmatizer()
def fonk1(tokens):
    return [b7.lemmatize(token) for token in tokens]
b8 = dict((ord(punct), None) for punct in string.punctuation)
def fonk2(text):
    return fonk1(nltk.word_tokenize(text.lower().translate(b8)))
b9 = ["My name is PyBot.", "My name is PyBot you can call me Pi.",
                 "I'b2 PyBot.", "My name is PyBot and my nickname is Pi. I am happy to solve your queries."]
b10 = ("hello", "hi", "greetings", "sup", "what's up", "hey")
b11 = ["hi", "hey", "hello", "I am glad! You are talking to me"]
b12 = ("what is python?",)
b13 = ("Python is a high-level, interpreted, interactive and object-oriented scripting programming language."
             " Python is designed to be highly readable. It uses English keywords frequently where as other "
             "languages use punctuation, and it has fewer syntactical constructions than other languages.")
b14 = ("what is module?", "what is module in python?")
b15 = ["Consider a module to be the same as a code library.",
              "A file containing a set of functions you want to include in your application.",
              "A module can define functions, classes and variables. A module can also include runnable code. "
              "Grouping related code into a module makes the code easier to understand and use."]
def fonk3(sentence):
    for word in sentence.split():
        if word.lower() in b10:
            return random.choice(b11)
def fonk4(sentence):
    if sentence.lower() in b12:
        return b13
def fonk5(sentence):
    if sentence.lower() in b14:
        return random.choice(b15)
def fonk6(sentence):
    return random.choice(b9)
def fonk7(b23, b5):
    b16 = ''
    b5.append(b23)
    b17 = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    b18 = b17.fit_transform(b5)
    b19 = cosine_similarity(b18[-1], b18)
    b20 = b19.argsort()[0][-2]
    b21 = b19.flatten()
    b21.sort()
    b22 = b21[-2]
    if b22 = = 0:
        b16 = "I am sorry! I don't understand you"
    else:
        b16 = b5[b20]
    return b16
def fonk8(b23):
    b23 = b23.lower()
    b24 = "module"
    if b23 != 'bye':
        if b23 = = 'thanks' or b23 == 'thank you':
            return "You are welcome.."
        elif fonk5(b23) is not None:
            return fonk5(b23)
        else:
            if b24 in b23:
                return fonk7(b23, b6)
            elif fonk3(b23) is not None:
                return fonk3(b23)
            elif "your name" in b23:
                return fonk6(b23)
            elif fonk4(b23) is not None:
                return fonk4(b23)
            else:
                return fonk7(b23, b5)
    else:
        return "Bye! take care.."
print("PyBot: Hello! I am PyBot. I will answer your queries about Python. If you want to exit, type Bye.")
while True:
    b25 = input("You: ")
    if b25.lower() == 'bye':
        print("PyBot: Bye! Take care..")
        break
    else:
        print("PyBot:", fonk8(b25))