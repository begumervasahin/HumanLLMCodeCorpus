import wikipedia
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import os
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))
pages_array = ['Alfa_Romeo', 'Aston_Martin', 'Audi', 'Automobile_Dacia', 'Bentley']
keyword_number = int(input('Broj Å¾eljenih najfrekventnijih kljuÄnih rijeÄi po dokumentu: '))
os.makedirs("Generated_txt", exist_ok=True)
dictionary = {}
def fetch_wikipedia_content(page_name):
    page = wikipedia.page(page_name)
    return page.content
def save_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
def read_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
def preprocess_text(text):
    words = word_tokenize(text)
    words_lowercase = [word.lower() for word in words if word.isalpha() or word.isnumeric()]
    lemmatized_words = [lemmatizer.lemmatize(word, pos="v") for word in words_lowercase if word not in stop_words]
    return lemmatized_words
def calculate_tfidf_weights(text, max_features):
    vectorizer = TfidfVectorizer(max_features=max_features)
    response = vectorizer.fit_transform([text])
    feature_names = vectorizer.get_feature_names_out()
    return response, feature_names
def save_tfidf_weights(file_path, response, feature_names):
    with open(file_path, 'w', encoding='utf-8') as file:
        for col in response.nonzero()[1]:
            file.write(f"{response[0, col]} - {feature_names[col]}\n")
def save_top_keywords(file_path, feature_names, response):
    with open(file_path, 'w', encoding='utf-8') as file:
        for col in response.nonzero()[1]:
            file.write(f"{feature_names[col]}\n")
for page_name in pages_array:
    document = fetch_wikipedia_content(page_name)
    original_text_file = os.path.join("Generated_txt", f"{page_name}.txt")
    save_to_file(original_text_file, document)
    contents = read_from_file(original_text_file)
    lemmatized_words = preprocess_text(contents)
    lemmatized_text = ", ".join(lemmatized_words)
    lemmatized_text_file = os.path.join("Generated_txt", f"{page_name}_Lemmatized.txt")
    save_to_file(lemmatized_text_file, lemmatized_text)
    print(f"{page_name:30} Broj rijeÄi: {len(lemmatized_words)}")
    response, feature_names = calculate_tfidf_weights(lemmatized_text, keyword_number)
    weights_text_file = os.path.join("Generated_txt", f"{page_name}_Weights.txt")
    save_tfidf_weights(weights_text_file, response, feature_names)
    top_keywords_text_file = os.path.join("Generated_txt", f"{page_name}_Top_Keywords.txt")
    save_top_keywords(top_keywords_text_file, feature_names, response)
    top_n_keywords = read_from_file(top_keywords_text_file).splitlines()
    dictionary[page_name] = top_n_keywords
    print("\n")
print("======================================== REPORT ========================================")
print(f"Preuzet tekst pojedine stranice sa Wikipedije, odraÄena lematizacija i izbacivanje stop rijeÄi, izraÄunate teÅ¾ine za {keyword_number} najfrekventnijih kljuÄnih rijeÄi. Generirano 4 .txt dokumenta za pojedinu Wikipedia stranicu.")
print("======================================== REPORT ========================================")