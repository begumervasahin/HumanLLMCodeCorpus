import nltk
import os
def remove_non_ascii(content):
    return ''.join([c for c in content if 32 <= ord(c) <= 126])
def collect_all_sentences(text_lines, sentence_splitter):
    print(f"Number of lines: {len(text_lines)}")
    sentences_tok = []
    for i, content in enumerate(text_lines):
        if (i + 1) % 1000 == 0:
            print(f"Progress: {(i + 1) / len(text_lines):.2%}")
        content_printable = remove_non_ascii(content).replace("Mr .", "Mr")
        sentences_raw = sentence_splitter.tokenize(content_printable)
        sentences_tok.extend(sentences_raw)
    return sentences_tok
def main():
    path_to_data = "/Users/ken77921/Desktop/TA/2004,7-05_nyt_tok"
    output_path = "/Users/ken77921/Desktop/TA/2004,7-05_nyt_sent"
    with open(path_to_data, 'r') as doc:
        text_lines = doc.readlines()
    sentence_splitter = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences_tok = collect_all_sentences(text_lines, sentence_splitter)
    with open(output_path, 'w') as f_out:
        for sent in sentences_tok:
            f_out.write(sent + '\n')
if __name__ == "__main__":
    main()