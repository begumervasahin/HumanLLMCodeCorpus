import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
def simplify_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    lemma = nltk.wordnet.WordNetLemmatizer()
    filtered_words = [lemma.lemmatize(word) for word in words if word not in stop_words]
    simplified_text = " ".join(filtered_words)
    return simplified_text
def calculate_similarity(text1, text2):
    vectorizer = TfidfVectorizer(min_df=1)
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity_score = (tfidf_matrix * tfidf_matrix.T).A[0, 1]
    return similarity_score
text1 = "hello I'm David, and I love my little bunny \n asdf fuck this code"
text2 = "hello I'm Juwon, and I love my big bear"
print("Similarity between text1 and text2:", calculate_similarity(text1, text2))
print("Similarity after simplification:", calculate_similarity(simplify_text(text1), simplify_text(text2)))
print("Example of simplified text:", simplify_text("hello I'm David, I was born on the best day of the best month because i'm the best of them all!"))