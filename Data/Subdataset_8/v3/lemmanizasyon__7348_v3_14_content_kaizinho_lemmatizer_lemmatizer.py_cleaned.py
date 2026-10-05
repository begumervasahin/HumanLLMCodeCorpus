import re
import json
def lemmatize(sentence, word_list):
    lemmatized_sentence = " ".join(word_list.get(word, word) for word in sentence.split())
    return lemmatized_sentence.strip()
def extract_words(raw_data_file, filename="data/swedish_words.json"):
    type_pattern = r"===(Verb|Substantiv|Adjektiv|Adverb|Konjuktion|Pronomen|Räkneord|Interjektion|Konjugation)==="
    word_pattern = r"'''([a-zA-ZåäöÅÄÖ]+)'''"
    lemma_pattern = r"'''([a-zA-ZåäöÅÄÖ]+)''' \(([^)]+)\)"
    data = {}
    current_type = None
    with open(raw_data_file, "r", encoding='utf-8') as input_file:
        for line in input_file:
            type_match = re.match(type_pattern, line)
            word_match = re.match(word_pattern, line)
            lemma_match = re.match(lemma_pattern, line)
            if type_match:
                current_type = type_match.group(1)
            elif word_match and current_type:
                word = word_match.group(1)
                data.setdefault(current_type, {})[word] = ""
            elif lemma_match and current_type:
                word = lemma_match.group(1)
                lemma = lemma_match.group(2)
                data.setdefault(current_type, {})[word] = lemma
    with open(filename, "w", encoding='utf-8') as output_file:
        json.dump(data, output_file, ensure_ascii=False, indent=4)
extract_words("raw_data_file.txt", "swedish_words.json")