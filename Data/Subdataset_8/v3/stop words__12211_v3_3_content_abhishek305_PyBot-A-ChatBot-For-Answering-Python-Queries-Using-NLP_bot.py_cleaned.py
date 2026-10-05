import nltk
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
with open('nlp_python_answer_finals.txt', 'r', errors='ignore') as python_file:
    python_responses = python_file.read().lower()
    python_sentences = nltk.sent_tokenize(python_responses)
with open('modules_pythons.txt', 'r', errors='ignore') as module_file:
    module_responses = module_file.read().lower()
    module_sentences = nltk.sent_tokenize(module_responses)
lemmatizer = nltk.stem.WordNetLemmatizer()
def lemmatize_tokens(tokens):
    return [lemmatizer.lemmatize(token) for token in tokens]
def normalize_text(text):
    tokens = nltk.word_tokenize(text.lower().translate(str.maketrans('', '', string.punctuation)))
    return lemmatize_tokens(tokens)
introduction_responses = ["My name is PyBot.", "You can call me Pi.", "I'm PyBot.", "I'm Pi, your friendly Python bot!"]
greeting_inputs = ("hello", "hi", "greetings", "sup", "what's up", "hey")
greeting_responses = ["Hi!", "Hey!", "Hello!", "I'm glad you're talking to me."]
basic_python_questions = ("what is python?",)
python_response = ("Python is a high-level, interpreted, interactive, and object-oriented programming language. "
                   "It's designed to be highly readable and uses English keywords extensively.")
basic_module_questions = ("what is module?", "what is module in python?")
module_responses = ["A module is like a code library.", "A module is a file containing functions or variables.",
                    "Modules help organize code and make it reusable."]
def respond_to_greeting(sentence):
    for word in sentence.split():
        if word.lower() in greeting_inputs:
            return random.choice(greeting_responses)
def respond_to_basic_python_question(sentence):
    if sentence.lower() in basic_python_questions:
        return python_response
def respond_to_basic_module_question(sentence):
    if sentence.lower() in basic_module_questions:
        return random.choice(module_responses)
def introduce_bot(sentence):
    return random.choice(introduction_responses)
def generate_response(user_input, sentences):
    response = ''
    sentences.append(user_input)
    tfidf_vectorizer = TfidfVectorizer(tokenizer=normalize_text, stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(sentences)
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix)
    most_similar_sentence_index = similarity_scores.argsort()[0][-2]
    flat_similarity_scores = similarity_scores.flatten()
    flat_similarity_scores.sort()
    highest_similarity_score = flat_similarity_scores[-2]
    if highest_similarity_score == 0:
        response = "I'm sorry, I don't understand."
    else:
        response = sentences[most_similar_sentence_index]
    return response
def chat(user_input):
    user_input = user_input.lower()
    module_keyword = "module"
    if user_input != 'bye':
        if user_input in ('thanks', 'thank you'):
            return "You're welcome!"
        elif respond_to_basic_module_question(user_input) is not None:
            return respond_to_basic_module_question(user_input)
        else:
            if module_keyword in user_input:
                return generate_response(user_input, module_sentences)
            elif respond_to_greeting(user_input) is not None:
                return respond_to_greeting(user_input)
            elif "your name" in user_input:
                return introduce_bot(user_input)
            elif respond_to_basic_python_question(user_input) is not None:
                return respond_to_basic_python_question(user_input)
            else:
                return generate_response(user_input, python_sentences)
    else:
        return "Goodbye! Take care."
print("PyBot: Hello! I'm PyBot, your friendly Python assistant. Feel free to ask me anything about Python.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("PyBot: Goodbye! Take care.")
        break
    else:
        print("PyBot:", chat(user_input))