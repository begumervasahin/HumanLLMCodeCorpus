import hashlib
import re
def main():
    input_file_path = 'data/test/ftb1/ftb1u.tsv'
    output_file_path = 'data/test/ftb1/ftb1u_sample.tsv'
    sentences = read_and_split_sentences(input_file_path)
    sampled_sentences = filter_sentences_by_sha256(sentences)
    print(f'Sampled {len(sampled_sentences)} out of {len(sentences)} sentences')
    write_sentences_to_file(output_file_path, sampled_sentences)
    print(f'Wrote samples to {output_file_path}')
def read_and_split_sentences(input_file_path):
    with open(input_file_path, 'r') as file:
        lines = file.readlines()
    return list(split_lines_into_sentences(lines))
def split_lines_into_sentences(lines):
    sentence = []
    for line in lines:
        if not line.strip() and sentence:
            yield ''.join(sentence).strip()
            sentence = []
        else:
            sentence.append(line)
    if sentence:
        yield ''.join(sentence).strip()
def filter_sentences_by_sha256(sentences):
    selected_sentences = []
    for sentence in sentences:
        digest = hashlib.sha256(sentence.encode('utf-8')).hexdigest()
        if digest.startswith('0'):
            selected_sentences.append(sentence)
    return selected_sentences
def write_sentences_to_file(output_file_path, sentences):
    with open(output_file_path, 'w') as file:
        for sentence in sentences:
            file.write(f"{sentence}\n")
if __name__ == '__main__':
    main()