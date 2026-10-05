import nltk
import warnings
import numpy as np
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
nltk.download('punkt')
nltk.download('wordnet')
warnings.filterwarnings("ignore")
with open('nlp_python_answer_finals.txt', 'r', b1 = 'ignore') as f:
    b2 = f.read().lower()
with open('modules_pythons.txt', 'r', b1 = 'ignore') as m:
    b3 = m.read().lower()
def fonk1(text):
    return nltk.sent_tokenize(text), nltk.word_tokenize(text)
sent_tokens, b4 = fonk1(b2)
sent_tokens_module, b5 = fonk1(b3)
b6 = nltk.stem.WordNetLemmatizer()
def fonk2(tokens):
    return [b6.fonk2(token) for token in tokens]
def fonk3(text):
    b7 = dict((ord(punct), None) for punct in string.punctuation)
    return fonk2(nltk.word_tokenize(text.lower().translate(b7)))
b8 = ("hello", "hi", "hey", "greetings", "sup", "what's up")
b9 = ["Hi", "Hey", "Hello", "I am glad you are talking to me"]
b10 = [
    "My name is PyBot.",
    "My name is PyBot you can call me Pi.",
    "I'm PyBot :)",
    "My name is PyBot and my nickname is Pi. I am happy to solve your queries :)"
]
b11 = {
    "what is python ?": "Python is a high-level, interpreted, interactive and object-oriented scripting programming language. Python is designed to be highly readable. It uses English keywords frequently whereas other languages use punctuation, and it has fewer syntactical constructions than other languages."
}
b12 = [
    ("what is module", "what is module?"),
    ("what is module?", "what is module?")
]
b13 = [
    "Consider a module to be the same as a code library.",
    "A file containing a set of functions you want to include in your application.",
    "A module can define functions, classes and variables. A module can also include runnable code. Grouping related code into a module makes the code easier to understand and use."
]
def fonk4(sentence):
    for word in sentence.split():
        if word.lower() in b8:
            return random.choice(b9)
def fonk5(sentence):
    for question, answer in b11.items():
        if sentence.lower() == question:
            return answer
def fonk6(sentence):
    for question_pair in b12:
        if sentence.lower() == question_pair[0] or sentence.lower() == question_pair[1]:
            return random.choice(b13)
def fonk7(sentence):
    return random.choice(b10)
def fonk8(b20, sent_tokens):
    b14 = ''
    sent_tokens.append(b20)
    b15 = TfidfVectorizer(tokenizer=normalize, stop_words='english')
    b16 = b15.fit_transform(sent_tokens)
    b17 = cosine_similarity(b16[-1], b16)
    b18 = b17.argsort()[0][-2]
    b19 = b17.flatten()[b18]
    if b19 = = 0:
        b14 = "I am sorry! I don't understand you"
    else:
        b14 = sent_tokens[b18]
    return b14
def fonk9(b20):
    b20 = b20.lower()
    b21 = "module"
    if b20 != 'bye':
        if b20 in ['thanks', 'thank you']:
            return "You are welcome.."
        elif fonk6(b20) is not None:
            return fonk6(b20)
        else:
            if b21 in b20:
                return fonk8(b20, sent_tokens_module)
            elif fonk4(b20) is not None:
                return fonk4(b20)
            elif "your name" in b20:
                return fonk7(b20)
            elif fonk5(b20) is not None:
                return fonk5(b20)
            else:
                return fonk8(b20, sent_tokens)
    else:
        return "Bye! take care.."
if b22 = = "__main__":
    while True:
        b23 = input("You: ")
        b24 = fonk9(b23)
        print("PyBot:", b24)
        if b23.lower() == 'bye':
            break