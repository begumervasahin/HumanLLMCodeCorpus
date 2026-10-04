import re
import json
def lemmatize(sentence, word_list):
    lemmatized_sentence = []
    for word in sentence.split():
        lemmatized_sentence.append(word_list.get(word, word))
    return ' '.join(lemmatized_sentence)
def extract_words(raw_data_file, output_file="data/swedish_words.json"):
    section_pattern = r"^(===(Verb|Substantiv|Adjektiv|Adverb|Konjuktion|Pronomen|RÃ¤kneord|Interjektion|Konjugation)===)$"
    word_pattern = r"^'''([a-zA-ZÃ¥Ã¤Ã¶Ã
ÃÃ]+)'''$"
    word_with_lemma_pattern = r"^'''([a-zA-ZÃ¥Ã¤Ã¶Ã
ÃÃ]+)''' \(([^)]+)\)$"
    data = {}
    current_type = None
    with open(raw_data_file, "r", encoding='utf-8') as input_file:
        for line in input_file:
            match = re.match(section_pattern, line)
            if match:
                current_type = match.group(2)
                data.setdefault(current_type, {})
            elif re.match(word_pattern, line) and current_type:
                word = re.match(word_pattern, line).group(1)
                data[current_type][word] = ""
            elif re.match(word_with_lemma_pattern, line) and current_type:
                match = re.match(word_with_lemma_pattern, line)
                word = match.group(1)
                lemma = match.group(2)
                data[current_type][word] = lemma
    with open(output_file, "w", encoding='utf-8') as output_file:
        json.dump(data, output_file, ensure_ascii=False, indent=4)
extract_words("raw_data_file.txt", "swedish_words.json")