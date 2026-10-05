import io
import string
import re
import nltk
from nltk.tag import tnt
from nltk.corpus import indian
input_file = open("tech_text_final.txt", "r")
output_file = open("output.txt", "w")
lemma_file = open("lemma.txt", "w+")
tag_file = open("tags.txt", "w")
word_dict = {}
def process_model():
    train_data = indian.tagged_sents('hindi.pos')
    tnt_pos_tagger = tnt.TnT()
    tnt_pos_tagger.train(train_data)
    text = input_file.read()
    sentences = text.split("à¥¤")
    for sentence in sentences:
        sentence = re.sub(r'(\d+)', r' ', sentence)
        sentence = sentence.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
        words = sentence.split()
        for word in words:
            if word.strip() != "":
                tagged_word = tnt_pos_tagger.tag(nltk.word_tokenize(word))
                output_file.write(word.rstrip() + "\n")
                tag_file.write(word.rstrip() + " : " + tagged_word[0][1] + "\n")
    tag_file.close()
    output_file.close()
def lemmatize():
    tag_data = open("tags.txt", "r")
    data = tag_data.read().split("\n")
    for token in data:
        if token == '':
            continue
        line = token.split(":")
        if line[1].strip().startswith("NN") or line[1].strip().startswith("PR") or line[1].strip().startswith("VAUX"):
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
    rule1 = suffixes[4][17]
    rule2 = suffixes[4][16]
    rule3 = suffixes[1][1]
    rule4 = suffixes[1][6]
    rule5 = suffixes[1][4]
    rule6 = suffixes[5][4]
    rule7 = suffixes[5][5]
    rule8 = suffixes[5][6]
    if word.endswith(rule1):
        word_dict[word] = [word[:word.rindex(rule1)] + suffixes[1][4]]
    elif word.endswith(rule2):
        word_dict[word] = [word[:word.rindex(rule2)] + suffixes[1][4]]
    elif word.endswith(rule3):
        word_dict[word] = [word[:word.rindex(rule3)] + suffixes[1][6]]
    elif word.endswith(rule4):
        word_dict[word] = [word[:word.rindex(rule4)] + suffixes[1][6]]
    elif word.endswith(rule5):
        word_dict[word] = [word[:word.rindex(rule5)] + suffixes[1][4]]
    elif word.endswith(rule6):
        word_dict[word] = [word[:word.rindex(rule6)] + suffixes[3][2]]
    elif word.endswith(rule7):
        word_dict[word] = [word[:word.rindex(rule7)] + suffixes[3][2]]
    elif word.endswith(rule8):
        word_dict[word] = [word[:word.rindex(rule8)] + suffixes[3][2]]
    else:
        if word_dict.get(word, None) == None:
            word_dict[word] = []
        for key in suffixes.keys():
            for value in suffixes[key]:
                if word.endswith(value):
                    suff = word.rindex(value)
                    word_dict[word].append(word[:suff])
def print_dict():
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