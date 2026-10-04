import re
import json
def lemmatize(sentence, word_list):
    words = sentence.split()
    lemmatized_sentence = " ".join(word_list.get(word, word) for word in words)
    return lemmatized_sentence
def extract_words(raw_data_file, output_file="swedish_words.json"):
    category_pattern = r"^(===(Verb|Substantiv|Adjektiv|Adverb|Konjuktion|Pronomen|RÃ¤kneord|Interjektion|Konjugation)===)$"
    word_pattern = r"^'''([a-zA-ZÃ¥Ã¤Ã¶Ã
ÃÃ]+)'''$"
    lemma_pattern = r"^'''([a-zA-ZÃ¥Ã¤Ã¶Ã
ÃÃ]+)''' \(([^)]+)\)$"
    data = {}
    current_category = None
    with open(raw_data_file, "r", encoding='utf-8') as input_file:
        for line in input_file:
            line = line.strip()
            if not line:
                continue
            category_match = re.match(category_pattern, line)
            word_match = re.match(word_pattern, line)
            lemma_match = re.match(lemma_pattern, line)
            if category_match:
                current_category = category_match.group(2)
                if current_category not in data:
                    data[current_category] = {}
            elif current_category and word_match:
                word = word_match.group(1)
                data[current_category][word] = ""
            elif current_category and lemma_match:
                word = lemma_match.group(1)
                lemma = lemma_match.group(2)
                data[current_category][word] = lemma
    with open(output_file, "w", encoding='utf-8') as output_file:
        json.dump(data, output_file, ensure_ascii=False, indent=4)
if __name__ == "__main__":
    extract_words("raw_data_file.txt", "swedish_words.json")