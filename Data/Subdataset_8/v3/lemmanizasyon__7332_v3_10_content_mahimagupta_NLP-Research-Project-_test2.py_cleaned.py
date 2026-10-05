import string
import re
import nltk
from nltk.tag import tnt
from nltk.corpus import indian
INPUT_FILE_PATH = "tech_text_final.txt"
OUTPUT_FILE_PATH = "output.txt"
LEMMA_FILE_PATH = "lemma.txt"
TAGS_FILE_PATH = "tags.txt"
with open(INPUT_FILE_PATH, "r", encoding="utf-8") as input_file:
    text = input_file.read()
output_file = open(OUTPUT_FILE_PATH, "w", encoding="utf-8")
lemma_file = open(LEMMA_FILE_PATH, "w+", encoding="utf-8")
tags_file = open(TAGS_FILE_PATH, "w", encoding="utf-8")
lemmatized_words = {}
def train_pos_tagger():
    train_data = indian.tagged_sents('hindi.pos')
    tnt_pos_tagger = tnt.TnT()
    tnt_pos_tagger.train(train_data)
    return tnt_pos_tagger
def process_text(tnt_pos_tagger):
    sentences = text.split("à¥¤")
    for sentence in sentences:
        sentence = re.sub(r'(\d+)', r' ', sentence)
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        words = sentence.split()
        for word in words:
            if word:
                tagged_word = tnt_pos_tagger.tag(nltk.word_tokenize(word))
                output_file.write(word.rstrip() + "\n")
                tags_file.write(word.rstrip() + " : " + tagged_word[0][1] + "\n")
def lemmatize_words():
    with open(TAGS_FILE_PATH, "r", encoding="utf-8") as tags:
        tagged_words = tags.read().split("\n")
    for tagged_word in tagged_words:
        if not tagged_word:
            continue
        word, tag = tagged_word.split(":")
        if tag.strip().startswith("NN") or tag.strip().startswith("PR") or tag.strip().startswith("VAUX"):
            lemmatized_words[word.strip()] = [word.strip()]
        else:
            generate_stem_words(word.strip())
def generate_stem_words(word):
    suffixes = {
        1: ["à¥", "à¥", "à¥", "à¥", "à¥", "à¤¿", "à¤¾"],
        2: ["à¤à¤°", "à¤¾à¤", "à¤¿à¤", "à¤¾à¤", "à¤¾à¤", "à¤¨à¥", "à¤¨à¥", "à¤¨à¤¾", "à¤¤à¥", "à¥à¤", "à¤¤à¥", "à¤¤à¤¾", "à¤¾à¤", "à¤¾à¤", "à¥à¤", "à¥à¤"],
        3: ["à¤¾à¤à¤°", "à¤¾à¤à¤", "à¤¾à¤à¤", "à¤¾à¤¯à¤¾", "à¥à¤à¥", "à¥à¤à¤¾", "à¥à¤à¥", "à¥à¤à¥", "à¤¾à¤¨à¥", "à¤¾à¤¨à¤¾", "à¤¾à¤¤à¥", "à¤¾à¤¤à¥", "à¤¾à¤¤à¤¾", "à¤¤à¥à¤", "à¤¾à¤à¤", "à¤¾à¤à¤", "à¥à¤à¤", "à¥à¤à¤", "à¥à¤à¤"],
        4: ["à¤¾à¤à¤à¥", "à¤¾à¤à¤à¤¾", "à¤¾à¤à¤à¥", "à¤¾à¤à¤à¥", "à¤à¤à¤à¥", "à¥à¤à¤à¥", "à¤à¤à¤à¥", "à¥à¤à¤à¥", "à¥à¤à¤à¥", "à¥à¤à¤à¤¾", "à¤¾à¤¤à¥à¤", "à¤¨à¤¾à¤à¤", "à¤¨à¤¾à¤à¤", "à¤¤à¤¾à¤à¤", "à¤¤à¤¾à¤à¤", "à¤¿à¤¯à¤¾à¤", "à¤¿à¤¯à¥à¤", "à¤¿à¤¯à¤¾à¤"],
        5: ["à¤¾à¤à¤à¤à¥", "à¤¾à¤à¤à¤à¥", "à¤¾à¤à¤à¤à¥", "à¤¾à¤à¤à¤à¤¾", "à¤¾à¤à¤¯à¤¾à¤", "à¤¾à¤à¤¯à¥à¤", "à¤¾à¤à¤¯à¤¾à¤"],
    }
    rule1 = suffixes[4][17]
    rule2 = suffixes[4][16]
    rule3 = suffixes[1][1]
    rule4 = suffixes[1][6]
    rule5 = suffixes[1][4]
    rule6 = suffixes[5][4]
    rule7 = suffixes[5][5]
    rule8 = suffixes[5][6]
    if word.endswith(rule1):
        lemmatized_words[word] = [word[:word.rindex(rule1)] + suffixes[1][4]]
    elif word.endswith(rule2):
        lemmatized_words[word] = [word[:word.rindex(rule2)] + suffixes[1][4]]
    elif word.endswith(rule3):
        lemmatized_words[word] = [word[:word.rindex(rule3)] + suffixes[1][6]]
    elif word.endswith(rule4):
        lemmatized_words[word] = [word[:word.rindex(rule4)] + suffixes[1][6]]
    elif word.endswith(rule5):
        lemmatized_words[word] = [word[:word.rindex(rule5)] + suffixes[1][4]]
    elif word.endswith(rule6):
        lemmatized_words[word] = [word[:word.rindex(rule6)] + suffixes[3][2]]
    elif word.endswith(rule7):
        lemmatized_words[word] = [word[:word.rindex(rule7)] + suffixes[3][2]]
    elif word.endswith(rule8):
        lemmatized_words[word] = [word[:word.rindex(rule8)] + suffixes[3][2]]
    else:
        if word not in lemmatized_words:
            lemmatized_words[word] = []
        for key in suffixes.keys():
            for value in suffixes[key]:
                if word.endswith(value):
                    suff_index = word.rindex(value)
                    lemmatized_words[word].append(word[:suff_index])
def write_lemmatized_words():
    for word, lemmas in lemmatized_words.items():
        if not lemmas:
            lemma_file.write(word + ": " + word)
        else:
            lemma_file.write(word + ": " + " ".join(set(lemmas)))
        lemma_file.write("\n")
def main():
    tnt_pos_tagger = train_pos_tagger()
    process_text(tnt_pos_tagger)
    lemmatize_words()
    write_lemmatized_words()
if __name__ == "__main__":
    main()