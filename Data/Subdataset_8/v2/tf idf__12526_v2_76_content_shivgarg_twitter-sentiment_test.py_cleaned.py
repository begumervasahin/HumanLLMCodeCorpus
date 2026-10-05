import sys
import nltk
import cPickle
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('stopwords')
with open('model/vector/vector.pkl', 'rb') as vectorizer_file:
    vectorizer = cPickle.load(vectorizer_file)
input_file_path = sys.argv[1] + '_twt'
output_file_path = sys.argv[2]
with open(input_file_path, 'r') as input_file:
    input_text = input_file.readlines()
transformed_input = vectorizer.transform(input_text)
with open('model/binary_lin.pkl', 'rb') as svm_model_file:
    svm_model = cPickle.load(svm_model_file)
predictions = svm_model.predict(transformed_input)
with open(output_file_path, 'w') as output_file:
    for prediction in predictions:
        output_file.write(str(prediction) + '\n')
print("Predictions have been written to", output_file_path)