import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
def simplify_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    word_list = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_text = [word for word in word_list if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    simplified_text = ' '.join([lemmatizer.lemmatize(word) for word in filtered_text])
    return simplified_text
def calculate_similarity(text1, text2):
    vectorizer = TfidfVectorizer(min_df=1)
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity_score = (tfidf_matrix * tfidf_matrix.T).A[0, 1]
    return similarity_score
if __name__ == "__main__":
    original_text1 = "hello I'm David, and I love my little bunny \n asdf this code"
    original_text2 = "hello I'm Juwon, and I love my big bear"
    simplified_text1 = simplify_text("hello I'm David, and I love my little bunny")
    simplified_text2 = simplify_text("hello I'm Juwon, and I love my big bear")
    print("Similarity between original texts:", calculate_similarity(original_text1, original_text2))
    print("Similarity between simplified texts:", calculate_similarity(simplified_text1, simplified_text2))
    print("Simplified text example:", simplify_text("hello I'm David, I was born on the best day of the best month because I'm the best of them all!"))