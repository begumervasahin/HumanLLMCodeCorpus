
import os
import json
import zipfile
import bisect
import sys
from nltk.stem import WordNetLemmatizer
from xml.etree.cElementTree import XML
WORD_NAMESPACE = '{http:
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'
ENGLISH_STOPWORDS = set(["i","me","my","myself","we","our","ours","ourselves","you","your","yours","yourself","yourselves","he","him","his","himself","she","her","hers","herself","it","its","itself","they","them","their","theirs","themselves","what","which","who","whom","this","that","these","those","am","is","are","was","were","be","been","being","have","has","had","having","do","does","did","doing","a","an","the","and","but","if","or","because","as","until","while","of","at","by","for","with","about","against","between","into","through","during","before","after","above","below","to","from","up","down","in","out","on","off","over","under","again","further","then","once","here","there","when","where","why","how","all","any","both","each","few","more","most","other","some","such","no","nor","not","only","own","same","so","than","too","very","s","t","can","will","just","don","should","now"])
def get_docx_text(path):
    with zipfile.ZipFile(path) as document:
        xml_content = document.read('word/document.xml')
    tree = XML(xml_content)
    paragraphs = [''.join(node.text for node in paragraph.getiterator(TEXT) if node.text) for paragraph in tree.getiterator(PARA)]
    return '\n\n'.join(paragraphs)
def remove_stopwords(wordlist):
    return [word for word in wordlist if word not in ENGLISH_STOPWORDS]
if len(sys.argv) < 2:
    print("Missing argument. Expected input docs directory as argument.\nEg: python create_index.py data")
    sys.exit()
input_docs_dir = sys.argv[1]
INDEX_FILE = "INDEX_FILE.INDEX"
index_dictionary = {}
lemmatizer = WordNetLemmatizer()
def add_to_postings(postings, docid):
    bisect.insort(postings, docid)
    return postings
for filename in os.listdir(input_docs_dir):
    if filename.endswith(".docx"):
        doc_text = get_docx_text(os.path.join(input_docs_dir, filename))
        word_tokens = remove_stopwords(doc_text.split())
        for word in word_tokens:
            lem_word = lemmatizer.lemmatize(word)
            index_dictionary.setdefault(lem_word, {'df': 0, 'postings': []})
            if filename not in index_dictionary[lem_word]['postings']:
                index_dictionary[lem_word]['df'] += 1
                index_dictionary[lem_word]['postings'] = add_to_postings(index_dictionary[lem_word]['postings'], filename)
with open(INDEX_FILE, 'w') as index_file:
    json.dump(index_dictionary, index_file, sort_keys=True)
print("Index file created at INDEX_FILE.INDEX")
print("Index stats\n" + '-' * 50)
print("Number of terms:", len(index_dictionary))