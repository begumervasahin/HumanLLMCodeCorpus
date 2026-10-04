import math
def calculate_cosine(vector1, vector2):
    if len(vector1) != len(vector2):
        return 0.0
    dot_product = sum(v1 * v2 for v1, v2 in zip(vector1, vector2))
    magnitude1 = math.sqrt(sum(v1 ** 2 for v1 in vector1))
    magnitude2 = math.sqrt(sum(v2 ** 2 for v2 in vector2))
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    return dot_product / (magnitude1 * magnitude2)
def read_lines(filepath):
    with open(filepath, 'r') as file:
        return [line.strip().lower() for line in file]
def main():
    dict_words = read_lines('dict_new.csv')
    documents = read_lines('doc.csv')
    stop_words = read_lines('stopword.txt')
    for doc in documents:
        print(doc)
    space_vector = [1] * len(dict_words)
    cosine_similarities = []
    with open('cos.csv', 'w') as output:
        for doc in documents:
            vector = [1 if word in doc else 0 for word in dict_words]
            cosine_similarity = calculate_cosine(vector, space_vector)
            output.write(f"{cosine_similarity}\n")
            cosine_similarities.append(cosine_similarity)
if __name__ == "__main__":
    main()