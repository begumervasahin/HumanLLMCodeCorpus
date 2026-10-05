import os
import nltk
import codecs
import subprocess
def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
def get_pdf_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            yield os.path.join(folder_path, filename)
def extract_text_from_pdfs(pdf_folder, corpus_folder):
    create_directory_if_not_exists(corpus_folder)
    for pdf_file in get_pdf_files(pdf_folder):
        text = extract_text_from_pdf(pdf_file)
        save_text_to_file(text, pdf_file, corpus_folder)
def extract_text_from_pdf(pdf_file):
    pdf2txt_path = os.path.join(os.getcwd(), 'pdf2txt.py')
    text = subprocess.check_output(['python', pdf2txt_path, pdf_file])
    return text.decode("utf-8").replace('\n', ' ').replace('\r', ' ').replace(',', ' ').replace('-', '').replace(':', ' ')
def save_text_to_file(text, pdf_file, corpus_folder):
    filename = os.path.splitext(os.path.basename(pdf_file))[0] + ".txt"
    output_path = os.path.join(corpus_folder, filename)
    with codecs.open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)
PDF_FOLDER = os.path.join(os.getcwd(), "pdf")
CORPUS_FOLDER = os.path.join(os.getcwd(), "corpus")
extract_text_from_pdfs(PDF_FOLDER, CORPUS_FOLDER)
corpus_reader = nltk.corpus.PlaintextCorpusReader(CORPUS_FOLDER, '.*\.txt')
word_freq_dist = nltk.FreqDist(corpus_reader.words())
total_word_count = sum(word_freq_dist.values())
vocab_size = len(word_freq_dist)
print('----------------------------------------------------------------------')
print("Corpus contains a vocabulary of {} and a word count of {}.".format(total_word_count, vocab_size))
print('----------------------------------------------------------------------')
print("Hapax legomena (words that appear only once):", word_freq_dist.hapaxes())
print('----------------------------------------------------------------------')
print("Most common words:", word_freq_dist.most_common(10))
print('----------------------------------------------------------------------')