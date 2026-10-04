import re
import json
def lemmatize(sentence, word_list):
    lemmatized_words = [word_list.get(word, word) for word in sentence.split()]
    return ' '.join(lemmatized_words)
def extract_words(raw_data_file, output_file="data/swedish_words.json"):
    section_pattern = re.compile(r"^===(Verb|Substantiv|Adjektiv|Adverb|Konjuktion|Pronomen|RÃ¤kneord|Interjektion|Konjugation)===$")
    word_pattern = re.compile(r"^'''([a-zA-ZÃ¥Ã¤Ã¶Ã
ÃÃ]+)'''$")
    word_with_lemma_pattern = re.compile(r"^'''([a-zA-ZÃ¥Ã¤Ã¶Ã
ÃÃ]+)''' \(([^)]+)\)$")
    data = {}
    current_type = None
    with open(raw_data_file, "r", encoding='utf-8') as input_file:
        for line in input_file:
            section_match = section_pattern.match(line)
            if section_match:
                current_type = section_match.group(1)
                if current_type not in data:
                    data[current_type] = {}
                continue
            word_match = word_pattern.match(line)
            if word_match and current_type:
                word = word_match.group(1)
                data[current_type][word] = ""
                continue
            word_with_lemma_match = word_with_lemma_pattern.match(line)
            if word_with_lemma_match and current_type:
                word, lemma = word_with_lemma_match.groups()
                data[current_type][word] = lemma
    with open(output_file, "w", encoding='utf-8') as output_file:
        json.dump(data, output_file, ensure_ascii=False, indent=4)
extract_words("raw_data_file.txt", "swedish_words.json")