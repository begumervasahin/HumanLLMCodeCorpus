
import spacy
import nltk
english_nlp_model = spacy.load('en')
stemming_tool = nltk.stem.PorterStemmer()
def compare_normalization(text_to_process):
    processed_text = english_nlp_model(text_to_process)
    lemmatized_tokens = [token.lemma_ for token in processed_text]
    stemmed_tokens = [stemming_tool.stem(token.norm_.lower()) for token in processed_text]
    print("Lemmatization:\n{}".format(lemmatized_tokens))
    print("Stemming:\n{}".format(stemmed_tokens))
example_text = "Our meeting today was worse than yesterday, I'm scared of meeting the clients tomorrow"
compare_normalization(example_text)