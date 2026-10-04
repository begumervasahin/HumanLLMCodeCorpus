import os
import subprocess
import codecs
import nltk
nltk_data_path = os.path.expanduser('~/nltk_data')
os.makedirs(nltk_data_path, exist_ok=True)
print(f"Does nltk_data path exist: {os.path.exists(nltk_data_path)}")
DOCS_PDF = os.path.join(os.getcwd(), "pdf")
CORPUS = os.path.join(os.getcwd(), "corpus")
def get_pdf_docs(path=DOCS_PDF):
    for name in os.listdir(path):
        if name.endswith('.pdf'):
            yield os.path.join(path, name)
def print_pdf_docs_count():
    pdf_docs = list(get_pdf_docs())
    print(f"Number of PDF documents found: {len(pdf_docs)}")
def extract_text_from_pdf(pdf_path):
    pdf2txt_script = os.path.join(os.getcwd(), 'pdf2txt.py')
    document = subprocess.check_output(['python', pdf2txt_script, pdf_path])
    return document.decode("utf-8")
def clean_text(text):
    return text.replace('\n', ' ').replace('\r', ' ').replace(',', ' ').replace('-', '').replace(':', ' ')
def save_text_to_file(text, output_path):
    with codecs.open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)
def extract_pdf_corpus(DOCS_PDF=DOCS_PDF, corpus_dir=CORPUS):
    os.makedirs(corpus_dir, exist_ok=True)
    for pdf_path in get_pdf_docs(DOCS_PDF):
        document_text = extract_text_from_pdf(pdf_path)
        cleaned_text = clean_text(document_text)
        txt_filename = os.path.splitext(os.path.basename(pdf_path))[0] + ".txt"
        txt_path = os.path.join(corpus_dir, txt_filename)
        save_text_to_file(cleaned_text, txt_path)
def analyze_corpus(corpus_dir=CORPUS):
    corpus = nltk.corpus.PlaintextCorpusReader(corpus_dir, '.*\.txt')
    words_freq_dist = nltk.FreqDist(corpus.words())
    total_word_count = sum(words_freq_dist.values())
    vocabulary_size = len(words_freq_dist)
    print('----------------------------------------------------------------------')
    print(f"Corpus contains a vocabulary of {vocabulary_size} and a word count of {total_word_count}.")
    print('----------------------------------------------------------------------')
    print("Hapaxes (words that appear only once):")
    print(words_freq_dist.hapaxes())
    print('----------------------------------------------------------------------')
    print("Most common words:")
    print(words_freq_dist.most_common())
print_pdf_docs_count()
extract_pdf_corpus()
analyze_corpus()