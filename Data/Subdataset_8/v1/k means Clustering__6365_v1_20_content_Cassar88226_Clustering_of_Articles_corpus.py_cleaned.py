import os
import nltk
import codecs
import subprocess
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
def get_pdf_docs(path):
    for name in os.listdir(path):
        if name.endswith('.pdf'):
            yield os.path.join(path, name)
def extract_pdf_corpus(docs_pdf, corpus):
    create_directory(corpus)
    for path in get_pdf_docs(docs_pdf):
        pdf2txt_path = os.path.join(os.getcwd(), 'pdf2txt.py')
        document = subprocess.check_output(['python', pdf2txt_path, path])
        filename = os.path.splitext(os.path.basename(path))[0] + ".txt"
        output_path = os.path.join(corpus, filename)
        document = document.decode("utf-8")
        document = document.replace('\n', ' ')
        document = document.replace('\r', ' ')
        document = document.replace(',', ' ')
        document = document.replace('-', '')
        document = document.replace(':', ' ')
        with codecs.open(output_path, 'w', encoding='utf-8') as f:
            f.write(document)
DOCS_PDF = os.path.join(os.getcwd(), "pdf")
CORPUS = os.path.join(os.getcwd(), "corpus")
extract_pdf_corpus(DOCS_PDF, CORPUS)
kddcorpus = nltk.corpus.PlaintextCorpusReader(CORPUS, '.*\.txt')
wordsvals = nltk.FreqDist(kddcorpus.words())
total_word_count = sum(wordsvals.values())
vocab_size = len(wordsvals)
print('----------------------------------------------------------------------')
print("Corpus contains a vocabulary of {} and a word count of {}.".format(total_word_count, vocab_size))
print('----------------------------------------------------------------------')
print("Hapax legomena (words that appear only once):", wordsvals.hapaxes())
print('----------------------------------------------------------------------')
print("Most common words:", wordsvals.most_common(10))
print('----------------------------------------------------------------------')