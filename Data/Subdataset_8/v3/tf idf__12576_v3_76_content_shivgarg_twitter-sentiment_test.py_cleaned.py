import sys
import nltk
import cPickle
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('stopwords')
def load_pickle(file_path):
    with open(file_path, 'rb') as file:
        return cPickle.load(file)
vectorizer_path = 'model/vector/vector.pkl'
vectorizer = load_pickle(vectorizer_path)
input_file_path = sys.argv[1] + '_twt'
output_file_path = sys.argv[2]
with open(input_file_path, 'r') as input_file:
    input_text = input_file.readlines()
transformed_input = vectorizer.transform(input_text)
svm_model_path = 'model/binary_lin.pkl'
svm_model = load_pickle(svm_model_path)
predictions = svm_model.predict(transformed_input)
with open(output_file_path, 'w') as output_file:
    for prediction in predictions:
        output_file.write(str(prediction) + '\n')
print("Predictions have been written to", output_file_path)