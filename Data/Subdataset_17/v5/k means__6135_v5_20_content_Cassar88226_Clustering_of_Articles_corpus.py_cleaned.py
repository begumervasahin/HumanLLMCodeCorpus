import os
import re
import nltk
import codecs
import subprocess
import unicodedata
def setup_nltk_data_path(path='~/nltk_data'):
    nltk_data_path = os.path.expanduser(path)
    if not os.path.exists(nltk_data_path):
        os.mkdir(nltk_data_path)
    print("Does path exist:", os.path.exists(nltk_data_path))
DOCS_PDF = os.path.join(os.getcwd(), "pdf")
CORPUS = os.path.join(os.getcwd(), "corpus")
def get_pdf_docs(path=DOCS_PDF):
    print("Searching for PDF files in:", path)
    return [os.path.join(path, name) for name in os.listdir(path) if name.endswith('.pdf')]
def extract_pdf_corpus(pdf_path=DOCS_PDF, corpus_path=CORPUS):
    if not os.path.exists(corpus_path):
        os.mkdir(corpus_path)
    pdf_files = get_pdf_docs(pdf_path)
    for pdf_file in pdf_files:
        script_path = os.path.join(os.getcwd(), 'pdf2txt.py')
        try:
            document = subprocess.check_output(['python', script_path, pdf_file])
            document_text = process_document_text(document.decode("utf-8"))
            text_filename = os.path.splitext(os.path.basename(pdf_file))[0] + ".txt"
            text_filepath = os.path.join(corpus_path, text_filename)
            save_text_to_file(text_filepath, document_text)
        except subprocess.CalledProcessError as e:
            print(f"Error processing {pdf_file}: {e}")
def process_document_text(text):
    text = text.replace('\n', ' ').replace('\r', ' ')
    text = text.replace(',', ' ').replace('-', '').replace(':', ' ')
    return text
def save_text_to_file(filepath, text):
    with codecs.open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
def analyze_corpus(corpus_path=CORPUS):
    kddcorpus = nltk.corpus.PlaintextCorpusReader(corpus_path, '.*\.txt')
    wordsvals = nltk.FreqDist(kddcorpus.words())
    word_count = sum(wordsvals.values())
    vocab_size = len(wordsvals)
    print_corpus_statistics(word_count, vocab_size, wordsvals)
def print_corpus_statistics(word_count, vocab_size, wordsvals):
    print('----------------------------------------------------------------------')
    print(f"Corpus contains a vocabulary of {vocab_size} and a word count of {word_count}.")
    print('----------------------------------------------------------------------')
    print("Hapaxes:", wordsvals.hapaxes())
    print('----------------------------------------------------------------------')
    print("Most common words:", wordsvals.most_common())
if __name__ == "__main__":
    setup_nltk_data_path()
    print("Number of PDF documents found:", len(get_pdf_docs()))
    extract_pdf_corpus()
    analyze_corpus()