import nltk
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
with open('nlp_python_answer_finals.txt', 'r', b1 = 'ignore') as python_file:
    b2 = python_file.read().lower()
    b3 = nltk.sent_tokenize(b2)
with open('modules_pythons.txt', 'r', b1 = 'ignore') as module_file:
    b4 = module_file.read().lower()
    b5 = nltk.sent_tokenize(b4)
b6 = nltk.stem.WordNetLemmatizer()
def fonk1(b7):
    return [b6.lemmatize(token) for token in b7]
def fonk2(text):
    b7 = nltk.word_tokenize(text.lower().translate(str.maketrans('', '', string.punctuation)))
    return fonk1(b7)
b8 = ["My name is PyBot.", "You can call me Pi.", "I'm PyBot.", "I'm Pi, your friendly Python bot!"]
b9 = ("hello", "hi", "greetings", "sup", "what's up", "hey")
b10 = ["Hi!", "Hey!", "Hello!", "I'm glad you're talking to me."]
b11 = ("what is python?",)
b12 = ("Python is a high-level, interpreted, interactive, and object-oriented programming language. "
                   "It's designed to be highly readable and uses English keywords extensively.")
b13 = ("what is module?", "what is module in python?")
b4 = ["A module is like a code library.", "A module is a file containing functions or variables.",
                    "Modules help organize code and make it reusable."]
def fonk3(sentence):
    for word in sentence.split():
        if word.lower() in b9:
            return random.choice(b10)
def fonk4(sentence):
    if sentence.lower() in b11:
        return b12
def fonk5(sentence):
    if sentence.lower() in b13:
        return random.choice(b4)
def fonk6(sentence):
    return random.choice(b8)
def fonk7(b21, sentences):
    b14 = ''
    sentences.append(b21)
    b15 = TfidfVectorizer(tokenizer=normalize_text, stop_words='english')
    b16 = b15.fit_transform(sentences)
    b17 = cosine_similarity(b16[-1], b16)
    b18 = b17.argsort()[0][-2]
    b19 = b17.flatten()
    b19.sort()
    b20 = b19[-2]
    if b20 = = 0:
        b14 = "I'm sorry, I don't understand."
    else:
        b14 = sentences[b18]
    return b14
def fonk8(b21):
    b21 = b21.lower()
    b22 = "module"
    if b21 != 'bye':
        if b21 in ('thanks', 'thank you'):
            return "You're welcome!"
        elif fonk5(b21) is not None:
            return fonk5(b21)
        else:
            if b22 in b21:
                return fonk7(b21, b5)
            elif fonk3(b21) is not None:
                return fonk3(b21)
            elif "your name" in b21:
                return fonk6(b21)
            elif fonk4(b21) is not None:
                return fonk4(b21)
            else:
                return fonk7(b21, b3)
    else:
        return "Goodbye! Take care."
print("PyBot: Hello! I'm PyBot, your friendly Python assistant. Feel free to ask me anything about Python.")
while True:
    b21 = input("You: ")
    if b21.lower() == 'bye':
        print("PyBot: Goodbye! Take care.")
        break
    else:
        print("PyBot:", fonk8(b21))