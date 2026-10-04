import os
import json
import codecs
import nltk
def get_relevant_sentences(relevant_docs, wiki_split_docs_dir):
    relevant_sentences = []
    for relevant_doc in relevant_docs:
        file_path = os.path.join(wiki_split_docs_dir, relevant_doc + ".json")
        with codecs.open(file_path, "r", "utf-8") as file:
            file_content = json.load(file)
            full_lines = file_content["lines"]
            lines = [line['content'].strip().replace("-LRB-", " ( ").replace("-RRB-", " ) ") for line in full_lines]
            for i, line in enumerate(lines):
                if line:
                    temp = {
                        'id': relevant_doc,
                        'line_num': i,
                        'sentence': line
                    }
                    relevant_sentences.append(temp)
    return relevant_sentences
def get_sentence(wiki_doc_dir, doc_filename, sentence_id):
    file_path = os.path.join(wiki_doc_dir, doc_filename + ".txt")
    with codecs.open(file_path, "r", "utf-8") as doc:
        doc_lines = doc.read().split("\n")
        return doc_lines[sentence_id].split("\t")[1]
