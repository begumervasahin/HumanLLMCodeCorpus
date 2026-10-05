import re
import string
from nltk.tag import tnt
from nltk.corpus import indian
import nltk
input_file = open("tech_text_final.txt", "r")
output_file = open("output.txt", "w")
lemma_file = open("lemma.txt", "w+")
tag_file = open("tags.txt", "w")
word_dict = {}
def preprocess_text(text):
    text = re.sub(r'(\d+)', r' ', text)
    text = text.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
    return text
def process_model():
    train_data = indian.tagged_sents('hindi.pos')
    tnt_pos_tagger = tnt.TnT()
    tnt_pos_tagger.train(train_data)
    text = input_file.read()
    sentences = text.split("à¥¤")
    for sentence in sentences:
        sentence = preprocess_text(sentence)
        words = nltk.word_tokenize(sentence)
        for word in words:
            if word.strip() != "":
                tagged_word = tnt_pos_tagger.tag([word])
                output_file.write(word.rstrip() + "\n")
                tag_file.write(word.rstrip() + " : " + tagged_word[0][1] + "\n")
    tag_file.close()
    output_file.close()
def lemmatize():
    with open("tags.txt", "r") as tag_data:
        data = tag_data.read().split("\n")
    for token in data:
        if token == '':
            continue
        line = token.split(":")
        if line[1].strip().startswith(("NN", "PR", "VAUX")):
            word_dict[line[0].strip()] = [line[0].strip()]
        else:
            generate_stem_words(line[0].strip())
def generate_stem_words(word):
    suffixes = {
        1: ["à¥", "à¥", "à¥", "à¥", "à¥", "à¤¿", "à¤¾"],
        2: ["à¤à¤°", "à¤¾à¤", "à¤¿à¤", "à¤¾à¤", "à¤¾à¤", "à¤¨à¥", "à¤¨à¥", "à¤¨à¤¾", "à¤¤à¥", "à¥à¤", "à¤¤à¥", "à¤¤à¤¾", "à¤¾à¤", "à¤¾à¤", "à¥à¤", "à¥à¤"],
        3: ["à¤¾à¤à¤°", "à¤¾à¤à¤", "à¤¾à¤à¤", "à¤¾à¤¯à¤¾", "à¥à¤à¥", "à¥à¤à¤¾", "à¥à¤à¥", "à¥à¤à¥", "à¤¾à¤¨à¥", "à¤¾à¤¨à¤¾", "à¤¾à¤¤à¥", "à¤¾à¤¤à¥", "à¤¾à¤¤à¤¾", "à¤¤à¥à¤", "à¤¾à¤à¤", "à¤¾à¤à¤", "à¥à¤à¤", "à¥à¤à¤", "à¥à¤à¤"],
        4: ["à¤¾à¤à¤à¥", "à¤¾à¤à¤à¤¾", "à¤¾à¤à¤à¥", "à¤¾à¤à¤à¥", "à¤à¤à¤à¥", "à¥à¤à¤à¥", "à¤à¤à¤à¥", "à¥à¤à¤à¥", "à¥à¤à¤à¥", "à¥à¤à¤à¤¾", "à¤¾à¤¤à¥à¤", "à¤¨à¤¾à¤à¤", "à¤¨à¤¾à¤à¤", "à¤¤à¤¾à¤à¤", "à¤¤à¤¾à¤à¤", "à¤¿à¤¯à¤¾à¤", "à¤¿à¤¯à¥à¤", "à¤¿à¤¯à¤¾à¤"],
        5: ["à¤¾à¤à¤à¤à¥", "à¤¾à¤à¤à¤à¥", "à¤¾à¤à¤à¤à¥", "à¤¾à¤à¤à¤à¤¾", "à¤¾à¤à¤¯à¤¾à¤", "à¤¾à¤à¤¯à¥à¤", "à¤¾à¤à¤¯à¤¾à¤"],
    }
    rules = [suffixes[4][17], suffixes[4][16], suffixes[1][1], suffixes[1][6], suffixes[1][4], suffixes[5][4], suffixes[5][5], suffixes[5][6]]
    for rule in rules:
        if word.endswith(rule):
            if rule == suffixes[4][17] or rule == suffixes[4][16] or rule == suffixes[1][4]:
                new_suffix = suffixes[1][4]
            elif rule == suffixes[1][1] or rule == suffixes[1][6]:
                new_suffix = suffixes[1][6]
            elif rule == suffixes[5][4] or rule == suffixes[5][5] or rule == suffixes[5][6]:
                new_suffix = suffixes[3][2]
            word_dict[word] = [word[:word.rindex(rule)] + new_suffix]
            return
    if word not in word_dict:
        word_dict[word] = []
def print_dict():
    with open("lemma.txt", "w+") as lemma_file:
        for k, v in word_dict.items():
            if not v:
                lemma_file.write(k + ": " + k)
            else:
                lemma_file.write(k + ": ")
                for element in set(v):
                    lemma_file.write(element + " ")
            lemma_file.write("\n")
def main():
    process_model()
    lemmatize()
    print_dict()
if __name__ == "__main__":
    main()