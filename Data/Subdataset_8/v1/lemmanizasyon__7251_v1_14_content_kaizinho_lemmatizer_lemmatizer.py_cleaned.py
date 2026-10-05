import re
import json
def lemmatize(sentence, word_list):
    lemm_sentence = ""
    for word in sentence.split():
        lemm_sentence += word_list.get(word, word) + " "
    return lemm_sentence.strip()
def extract_words(raw_data_file, filename="data/swedish_words.json"):
    pattern1 = r"^(===(Verb|Substantiv|Adjektiv|Adverb|Konjuktion|Pronomen|RÃ¤kneord|Interjektion|Konjugation)===)$"
    pattern2 = r"^'''([a-zA-ZÃ¥Ã¤Ã¶Ã
ÃÃ]+)'''$"
    pattern3 = r"^'''([a-zA-ZÃ¥Ã¤Ã¶Ã
ÃÃ]+)''' \(([^)]+)\)$"
    data = {}
    current_type = None
    with open(raw_data_file, "r", encoding='utf-8') as input_file:
        for line in input_file:
            match1 = re.match(pattern1, line)
            match2 = re.match(pattern2, line)
            match3 = re.match(pattern3, line)
            if match1:
                current_type = match1.group(2)
            elif match2 and current_type:
                word = match2.group(1)
                if current_type not in data:
                    data[current_type] = {}
                data[current_type][word] = ""
            elif match3 and current_type:
                word = match3.group(1)
                lemma = match3.group(2)
                if current_type not in data:
                    data[current_type] = {}
                data[current_type][word] = lemma
    with open(filename, "w", encoding='utf-8') as output_file:
        json.dump(data, output_file, ensure_ascii=False, indent=4)
extract_words("raw_data_file.txt", "swedish_words.json")