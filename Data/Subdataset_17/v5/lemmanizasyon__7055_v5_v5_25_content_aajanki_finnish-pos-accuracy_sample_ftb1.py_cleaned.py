import hashlib
def main():
    input_file_path = 'data/test/ftb1/ftb1u.tsv'
    output_file_path = 'data/test/ftb1/ftb1u_sample.tsv'
    sentences = read_sentences_from_file(input_file_path)
    sentences = split_text_into_sentences(sentences)
    filtered_sentences = filter_sentences_by_sha256(sentences)
    print(f'Sampled {len(filtered_sentences)} out of {len(sentences)} sentences')
    write_sentences_to_file(output_file_path, filtered_sentences)
    print(f'Wrote samples to {output_file_path}')
def read_sentences_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()
def split_text_into_sentences(lines):
    sentences = []
    current_sentence = []
    for line in lines:
        stripped_line = line.strip()
        if not stripped_line and current_sentence:
            sentences.append(' '.join(current_sentence).strip())
            current_sentence = []
        else:
            current_sentence.append(line.strip())
    if current_sentence:
        sentences.append(' '.join(current_sentence).strip())
    return sentences
def filter_sentences_by_sha256(sentences):
    filtered = []
    for sentence in sentences:
        hash_digest = hashlib.sha256(sentence.encode('utf-8')).hexdigest()
        if hash_digest.startswith('0'):
            filtered.append(sentence)
    return filtered
def write_sentences_to_file(file_path, sentences):
    with open(file_path, 'w') as file:
        file.write('\n'.join(sentences) + '\n')
if __name__ == '__main__':
    main()