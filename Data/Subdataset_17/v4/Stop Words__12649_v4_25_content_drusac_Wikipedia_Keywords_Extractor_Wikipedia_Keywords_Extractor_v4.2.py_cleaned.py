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
dictionary = {}
for page_name in pages_array:
    page = wikipedia.page(page_name)
    document = page.content
    raw_file_path = os.path.join(output_dir, f"{page_name}.txt")
    with open(raw_file_path, 'w', encoding='utf-8') as file:
        file.write(document)
    with open(raw_file_path, "r", encoding='utf-8') as file:
        contents = file.read()
        words = word_tokenize(contents)
    words_lowercase = [word.lower() for word in words if word.isalpha() or word.isnumeric()]
    lemmatized_words = [lemmatizer.lemmatize(word, pos="v") for word in words_lowercase if word not in stop_words]
    lemmatized_file_path = os.path.join(output_dir, f"{page_name}_Lemmatized.txt")
    with open(lemmatized_file_path, 'w', encoding='utf-8') as file:
        file.write(", ".join(lemmatized_words))
    print(f"{page_name:30} Broj rijeÄi: {len(lemmatized_words):5}")
    vectorizer = TfidfVectorizer(max_features=keyword_number)
    response = vectorizer.fit_transform([" ".join(lemmatized_words)])
    weights_file_path = os.path.join(output_dir, f"{page_name}_Weights.txt")
    with open(weights_file_path, 'w', encoding='utf-8') as file:
        for col in response.nonzero()[1]:
            file.write(f"{response[0, col]} - {vectorizer.get_feature_names_out()[col]}\n")
    top_keywords_file_path = os.path.join(output_dir, f"{page_name}_Top_Keywords.txt")
    top_keywords = [vectorizer.get_feature_names_out()[col] for col in response.nonzero()[1]]
    with open(top_keywords_file_path, 'w', encoding='utf-8') as file:
        file.write("\n".join(top_keywords))
    dictionary[page_name] = top_keywords
    print("\n".join(top_keywords))
    print("\n")
print("="*88)
print("REPORT")
print("Preuzet tekst pojedine stranice sa Wikipedije, odraÄena lematizacija i izbacivanje stop rijeÄi, izraÄunate teÅ¾ine za", keyword_number, "najfrekventnijih kljuÄnih rijeÄi. Generirano 4 .txt dokumenta za pojedinu Wikipedia stranicu.")
print("="*88)
print("\n\n")