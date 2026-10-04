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
for page_name in pages_array:
    page = wikipedia.page(page_name)
    document = page.content
    original_text_file = os.path.join("Generated_txt", f"{page_name}.txt")
    with open(original_text_file, 'w', encoding='utf-8') as file:
        file.write(document)
    with open(original_text_file, 'r', encoding='utf-8') as file:
        contents = file.read()
    words = word_tokenize(contents)
    words_lowercase = [word.lower() for word in words if word.isalpha() or word.isnumeric()]
    lemmatized_words = [lemmatizer.lemmatize(word, pos="v") for word in words_lowercase if word not in stop_words]
    lemmatized_text_file = os.path.join("Generated_txt", f"{page_name}_Lemmatized.txt")
    with open(lemmatized_text_file, 'w', encoding='utf-8') as file:
        file.write(", ".join(lemmatized_words))
    print(f"{page_name:30} Broj rijeÄi: {len(lemmatized_words)}")
    with open(lemmatized_text_file, 'r', encoding='utf-8') as file:
        contents = file.read()
    vectorizer = TfidfVectorizer(max_features=keyword_number)
    response = vectorizer.fit_transform([contents])
    feature_names = vectorizer.get_feature_names_out()
    weights_text_file = os.path.join("Generated_txt", f"{page_name}_Weights.txt")
    with open(weights_text_file, 'w', encoding='utf-8') as file:
        for col in response.nonzero()[1]:
            file.write(f"{response[0, col]} - {feature_names[col]}\n")
    top_keywords_text_file = os.path.join("Generated_txt", f"{page_name}_Top_Keywords.txt")
    with open(top_keywords_text_file, 'w', encoding='utf-8') as file:
        for col in response.nonzero()[1]:
            file.write(f"{feature_names[col]}\n")
    with open(top_keywords_text_file, 'r', encoding='utf-8') as file:
        top_n_keywords = file.read().splitlines()
    dictionary[page_name] = top_n_keywords
    print("\n")
print("======================================== REPORT ========================================")
print(f"Preuzet tekst pojedine stranice sa Wikipedije, odraÄena lematizacija i izbacivanje stop rijeÄi, izraÄunate teÅ¾ine za {keyword_number} najfrekventnijih kljuÄnih rijeÄi. Generirano 4 .txt dokumenta za pojedinu Wikipedia stranicu.")
print("======================================== REPORT ========================================")