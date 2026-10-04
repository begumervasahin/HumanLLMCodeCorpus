
import sys
import os
import math
from docopt import docopt
from utils import process_document_words, process_document_ngrams, get_documents, extract_vocab, top_cond_probs_by_author
def count_docs(documents):
    return len(documents)
def count_docs_in_class(documents, class_name):
    return sum(1 for values in documents.values() if values[0] == class_name)
def concatenate_text_of_all_docs_in_class(documents, class_name):
    words_in_class = {}
    for values in documents.values():
        if values[0] == class_name:
            for word, freq in values[2].items():
                words_in_class[word] = words_in_class.get(word, 0) + freq
    return words_in_class
def train_naive_bayes(classes, documents, alpha=0.1):
    vocabulary = extract_vocab(documents)
    conditional_probabilities = {t: {} for t in vocabulary}
    priors = {}
    print("\n\n***\nCalculating priors and conditional probabilities for each class...\n***")
    for class_name in classes:
        priors[class_name] = count_docs_in_class(documents, class_name) / count_docs(documents)
        print(f"\nPrior for {class_name}: {priors[class_name]}")
        class_size = count_docs_in_class(documents, class_name)
        print(f"In class {class_name}, we have {class_size} document(s).")
        words_in_class = concatenate_text_of_all_docs_in_class(documents, class_name)
        print("Calculating conditional probabilities for the vocabulary.")
        denominator = sum(words_in_class.values())
        for t in vocabulary:
            conditional_probabilities[t][class_name] = (
                (words_in_class.get(t, 0) + alpha) /
                (denominator + alpha * len(vocabulary))
            )
    return vocabulary, priors, conditional_probabilities
def apply_naive_bayes(classes, vocabulary, priors, conditional_probabilities, test_document, feature_type, ngram_size):
    scores = {}
    if feature_type == "chars":
        _, _, words = process_document_ngrams(test_document, ngram_size)
    else:
        _, _, words = process_document_words(test_document)
    for class_name in classes:
        scores[class_name] = math.log(priors[class_name])
        for word in words:
            if word in conditional_probabilities:
                scores[class_name] += words[word] * math.log(conditional_probabilities[word][class_name])
    print("\n\nNow printing scores in descending order:")
    for author in sorted(scores, key=scores.get, reverse=True):
        print(f"{author} score: {scores[author]}")
if __name__ == '__main__':
    arguments = docopt(__doc__, version='Authorship Attribution 1.1')
    feature_type = "words" if arguments["--words"] else "chars"
    ngram_size = int(arguments["--chars"]) if arguments["--chars"] else -1
    testfile = arguments["<filename>"]
    alpha = 0.1
    classes = ["Austen", "Carroll", "Grahame", "Shelley"]
    documents = get_documents(feature_type, ngram_size)
    vocabulary, priors, conditional_probabilities = train_naive_bayes(classes, documents, alpha)
    for author in classes:
        print(f"\nBest features for {author}")
        top_cond_probs_by_author(conditional_probabilities, author, 10)
    apply_naive_bayes(classes, vocabulary, priors, conditional_probabilities, testfile, feature_type, ngram_size)