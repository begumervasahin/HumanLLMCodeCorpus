import wikipedia
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import os
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))
pages_array = ['Alfa_Romeo', 'Aston_Martin', 'Audi', 'Automobile_Dacia', 'Bentley']
output_dir = "Generated_txt"
os.makedirs(output_dir, exist_ok=True)
keyword_number = int(input('Broj Å¾eljenih najfrekventnijih kljuÄnih rijeÄi po dokumentu: '))
top_keywords_dict = {}
def save_text_to_file(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)
def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
def tokenize_and_filter_text(text):
    words = word_tokenize(text)
    return [word.lower() for word in words if word.isalpha() or word.isnumeric()]
def lemmatize_and_remove_stopwords(words):
    return [lemmatizer.lemmatize(word, pos="v") for word in words if word not in stop_words]
def calculate_tfidf_and_get_top_keywords(text, num_keywords):
    vectorizer = TfidfVectorizer(max_features=num_keywords)
    response = vectorizer.fit_transform([text])
    feature_names = vectorizer.get_feature_names_out()
    top_keywords = [feature_names[col] for col in response.nonzero()[1]]
    weights = {feature_names[col]: response[0, col] for col in response.nonzero()[1]}
    return top_keywords, weights
for page_name in pages_array:
    page = wikipedia.page(page_name)
    document = page.content
    raw_file_path = os.path.join(output_dir, f"{page_name}.txt")
    save_text_to_file(raw_file_path, document)
    contents = read_text_from_file(raw_file_path)
    words_lowercase = tokenize_and_filter_text(contents)
    lemmatized_words = lemmatize_and_remove_stopwords(words_lowercase)
    lemmatized_file_path = os.path.join(output_dir, f"{page_name}_Lemmatized.txt")
    save_text_to_file(lemmatized_file_path, ", ".join(lemmatized_words))
    print(f"{page_name:30} Broj rijeÄi: {len(lemmatized_words):5}")
    top_keywords, weights = calculate_tfidf_and_get_top_keywords(" ".join(lemmatized_words), keyword_number)
    weights_file_path = os.path.join(output_dir, f"{page_name}_Weights.txt")
    save_text_to_file(weights_file_path, "\n".join([f"{weight} - {word}" for word, weight in weights.items()]))
    top_keywords_file_path = os.path.join(output_dir, f"{page_name}_Top_Keywords.txt")
    save_text_to_file(top_keywords_file_path, "\n".join(top_keywords))
    top_keywords_dict[page_name] = top_keywords
    print("\n".join(top_keywords))
    print("\n")
print("=" * 88)
print("REPORT")
print(f"Preuzet tekst pojedine stranice sa Wikipedije, odraÄena lematizacija i izbacivanje stop rijeÄi, izraÄunate teÅ¾ine za {keyword_number} najfrekventnijih kljuÄnih rijeÄi. Generirano 4 .txt dokumenta za pojedinu Wikipedia stranicu.")
print("=" * 88)
print("\n\n")