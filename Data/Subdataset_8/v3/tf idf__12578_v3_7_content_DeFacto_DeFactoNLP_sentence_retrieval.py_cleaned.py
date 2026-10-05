import os
import json
import codecs
def get_relevant_sentences(relevant_docs, entities, wiki_split_docs_dir):
    relevant_sentences = []
    for doc_id in relevant_docs:
        with codecs.open(os.path.join(wiki_split_docs_dir, f"{doc_id}.json"), "r", "utf-8") as file:
            doc_data = json.load(file)
            lines = doc_data.get("lines", [])
            for line_num, line in enumerate(lines):
                content = line.get('content', '').strip()
                if content:
                    content = content.replace("-LRB-", " ( ").replace("-RRB-", " ) ")
                    sentence_info = {'id': doc_id, 'line_num': line_num, 'sentence': content}
                    relevant_sentences.append(sentence_info)
    return relevant_sentences
def get_sentence(wiki_doc_dir, doc_filename, sentence_id):
    with codecs.open(os.path.join(wiki_doc_dir, f"{doc_filename}.txt"), "r", "utf-8") as doc_file:
        doc_lines = doc_file.read().splitlines()
        if 0 <= sentence_id < len(doc_lines):
            return doc_lines[sentence_id].split("\t")[1]
        else:
            return None
relevant_docs = ["doc1", "doc2"]
entities = ["entity1", "entity2"]
wiki_split_docs_dir = "path/to/wiki/split/docs"
relevant_sentences = get_relevant_sentences(relevant_docs, entities, wiki_split_docs_dir)
print(relevant_sentences)
sentence = get_sentence("path/to/wiki/docs", "example_doc", 3)
print(sentence)