import os
import json
import codecs
def get_relevant_sentences(relevant_docs, wiki_split_docs_dir):
    relevant_sentences = []
    for doc in relevant_docs:
        file_path = os.path.join(wiki_split_docs_dir, f"{doc}.json")
        with codecs.open(file_path, "r", "utf-8") as file:
            content = json.load(file)
            lines = content["lines"]
            for i, line in enumerate(lines):
                sentence = line['content'].strip()
                sentence = sentence.replace("-LRB-", " ( ").replace("-RRB-", " ) ")
                if sentence:
                    relevant_sentences.append({
                        'id': doc,
                        'line_num': i,
                        'sentence': sentence
                    })
    return relevant_sentences
def get_sentence(wiki_doc_dir, doc_filename, sentence_id):
    file_path = os.path.join(wiki_doc_dir, f"{doc_filename}.txt")
    with codecs.open(file_path, "r", "utf-8") as doc:
        lines = doc.read().split("\n")
        if 0 <= sentence_id < len(lines):
            return lines[sentence_id].split("\t")[1]
        else:
            raise IndexError("Sentence ID out of range")
