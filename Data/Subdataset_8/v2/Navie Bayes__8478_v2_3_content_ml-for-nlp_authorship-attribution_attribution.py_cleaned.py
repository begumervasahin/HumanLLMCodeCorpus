import sys
import math
from utils import process_document_words, process_document_ngrams, get_documents, extract_vocab, top_cond_probs_by_author
from docopt import docopt
def count_documents(documents):
    return len(documents)
def count_documents_in_class(documents, class_label):
    count = sum(1 for _, (label, _) in documents.items() if label == class_label)
    return count
def concatenate_text_of_all_docs_in_class(documents, class_label):
    words_in_class = {}
    for doc_id, (label, word_freq) in documents.items():
        if label == class_label:
            for word, freq in word_freq.items():
                words_in_class[word] = words_in_class.get(word, 0) + freq
    return words_in_class
def train_naive_bayes(classes, documents, alpha=0.1):
    vocabulary = extract_vocab(documents)
    conditional_probabilities = {word: {c: 0 for c in classes} for word in vocabulary}
    priors = {}
    print("\n\n***\nCalculating priors and conditional probabilities for each class...\n***")
    total_documents = count_documents(documents)
    for c in classes:
        priors[c] = count_documents_in_class(documents, c) / total_documents
        print("\nPrior for", c, priors[c])
        class_size = count_documents_in_class(documents, c)
        print("In class", c, "we have", class_size, "document(s).")
        words_in_class = concatenate_text_of_all_docs_in_class(documents, c)
        print("Calculating conditional probabilities for the vocabulary.")
        denominator = sum(words_in_class.values())
        for t in vocabulary:
            if t in words_in_class:
                conditional_probabilities[t][c] = (words_in_class[t] + alpha) / (denominator + alpha * len(vocabulary))
            else:
                conditional_probabilities[t][c] = alpha / (denominator + alpha * len(vocabulary))
    return vocabulary, priors, conditional_probabilities
def apply_naive_bayes(classes, vocabulary, priors, conditional_probabilities, test_document, feature_type="words", ngram_size=-1):
    scores = {}
    if feature_type == "chars":
        author, doc_length, words = process_document_ngrams(test_document, ngram_size)
    elif feature_type == "words":
        author, doc_length, words = process_document_words(test_document)
    for c in classes:
        scores[c] = math.log(priors[c])
        for t in words:
            if t in conditional_probabilities:
                scores[c] += words[t] * math.log(conditional_probabilities[t][c])
    print("\n\nNow printing scores in descending order:")
    for author in sorted(scores, key=scores.get, reverse=True):
        print(author, "score:", scores[author])
if __name__ == '__main__':
    arguments = docopt(__doc__, version='Authorship Attribution 1.1')
    if arguments["--words"]:
        feature_type = "words"
        ngram_size = -1
    if arguments["--chars"]:
        feature_type = "chars"
        ngram_size = int(arguments["--chars"])
    testfile = arguments["<filename>"]
    classes = ["Austen", "Carroll", "Grahame", "Shelley"]
    documents = get_documents(feature_type, ngram_size)
    vocabulary, priors, conditional_probabilities = train_naive_bayes(classes, documents)
    for author in classes:
        print("\nBest features for", author)
        top_cond_probs_by_author(conditional_probabilities, author, 10)
    apply_naive_bayes(classes, vocabulary, priors, conditional_probabilities, testfile, feature_type, ngram_size)