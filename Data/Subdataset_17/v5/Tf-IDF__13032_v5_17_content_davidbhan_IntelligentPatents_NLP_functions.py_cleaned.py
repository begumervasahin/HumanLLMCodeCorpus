import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
def simplify_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    word_list = nltk.word_tokenize(text)
    filtered_words = [word for word in word_list if word not in stopwords.words('english')]
    lemmatizer = nltk.wordnet.WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
    simplified_text = ' '.join(lemmatized_words)
    return simplified_text
def calculate_similarity(text1, text2):
    vectorizer = TfidfVectorizer(min_df=1)
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity_score = (tfidf_matrix * tfidf_matrix.T).A[0, 1]
    return similarity_score
text1 = "hello I'm David, and I love my little bunny \n asdf fuck this code"
text2 = "hello I'm Juwon, and I love my big bear"
simplified_text1 = simplify_text("hello I'm David, and I love my little bunny")
simplified_text2 = simplify_text("hello I'm Juwon, and I love my big bear")
simplified_text3 = simplify_text("hello I'm David, I was born on the best day of the best month because I'm the best of them all!")
print(calculate_similarity(text1, text2))
print(calculate_similarity(simplified_text1, simplified_text2))
print(simplified_text3)