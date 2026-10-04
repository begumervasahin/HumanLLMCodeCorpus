import wikipedia
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import networkx as nx
import matplotlib.pyplot as plt
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))
pages_array = ['Alfa_Romeo', 'Aston_Martin', 'Audi', 'Automobile_Dacia', 'Bentley']
print("\n")
keyword_number = int(input('Broj Å¾eljenih najfrekventnijih kljuÄnih rijeÄi po dokumentu: '))
save_to_counter = 0
dictionary = {}
for i in pages_array:
    page = wikipedia.page(i)
    document = page.content
    add_text_extension = str(i) + ".txt"
    file = open("Generated_txt/" + add_text_extension, 'w', encoding = 'utf-8')
    file.write(document)
    file.close()
    file = open("Generated_txt/" + add_text_extension, "r", encoding = 'utf-8')
    contents = file.read()
    words = word_tokenize(contents)
    file.close()
    words_lowercase = [word.lower() for word in words if word.isalpha() or word.isnumeric()]
    add_name_lemmatized = str(i) + "_Lemmatized.txt"
    file = open("Generated_txt/" + add_name_lemmatized, 'w', encoding = 'utf-8')
    x = 0
    for word in words_lowercase:
        lemmatized_word = lemmatizer.lemmatize(word, pos = "v")
        if lemmatized_word not in stop_words:
            file.write(lemmatized_word)
            file.write(", ")
            x += 1
    file.close()
    print("{0:30}{1:5}{2:7}".format(i, "Broj rijeÄi:", x))
    file = open("Generated_txt/" + add_name_lemmatized, 'r', encoding = 'utf-8')
    contents = file.read()
    vectorizer = TfidfVectorizer(max_features = keyword_number)
    response = vectorizer.fit_transform([contents])
    file.close()
    add_name_weights = str(i) + "_Weights.txt"
    file = open("Generated_txt/" + add_name_weights, 'w', encoding = 'utf-8')
    add_name_top_keywords = str(i) + "_Top_Keywords.txt"
    file = open("Generated_txt/" + add_name_top_keywords, 'w', encoding = 'utf-8')
    feature_names = vectorizer.get_feature_names()
    for col in response.nonzero()[1]:
        print (feature_names[col], ' - ', response[0, col])
    with open("Generated_txt/" + add_name_weights, 'w') as f:
        for col in response.nonzero()[1]:
            print(response[0, col], ' - ', feature_names[col], file = f)
    with open("Generated_txt/" + add_name_top_keywords, 'w') as f:
        for col in response.nonzero()[1]:
            print(feature_names[col], file = f)
    file = open("Generated_txt/" + add_name_top_keywords, 'r')
    top_n_keywords = file.read().splitlines()
    print("\n")
    dictionary["{}".format(i)]= top_n_keywords
    file.close()
print("======================================== REPORT ========================================\nPreuzet tekst pojedine stranice sa Wikipedije, odraÄena lematizacija i izbacivanje stop rijeÄi, izraÄunate teÅ¾ine za", keyword_number, "najfrekventnijih kljuÄnih rijeÄi. Generirano 4 .txt dokumenta za pojedinu Wikipedia stranicu.\n======================================== REPORT ========================================")
print("\n\n")
print("\n\n")
print("\n\n")