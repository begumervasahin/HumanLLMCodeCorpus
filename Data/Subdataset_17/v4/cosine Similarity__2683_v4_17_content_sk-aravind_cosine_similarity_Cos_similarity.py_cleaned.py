from collections import Counter
import math
THRESHOLD = 0.4
def counter_cosine_similarity(c1, c2):
    terms = set(c1).union(c2)
    dot_product = sum(c1.get(term, 0) * c2.get(term, 0) for term in terms)
    magnitude_a = math.sqrt(sum(c1.get(term, 0)**2 for term in terms))
    magnitude_b = math.sqrt(sum(c2.get(term, 0)**2 for term in terms))
    if magnitude_a * magnitude_b == 0:
        return 0.0
    return dot_product / (magnitude_a * magnitude_b)
def length_similarity(c1, c2):
    len_c1 = sum(c1.values())
    len_c2 = sum(c2.values())
    return min(len_c1, len_c2) / float(max(len_c1, len_c2))
def similarity_score(l1, l2):
    c1, c2 = Counter(l1), Counter(l2)
    score_prob = length_similarity(c1, c2) * counter_cosine_similarity(c1, c2)
    print(f"Similarity Score: {score_prob:.2f}")
    if score_prob > THRESHOLD:
        print("Status: still doing work")
    else:
        print("Status: Fuck you do work")
def main():
    input_model = "algorithms node current shortest path lol"
    input_current = "shortest node current"
    model_words = input_model.split()
    current_words = input_current.split()
    similarity_score(model_words, current_words)
if __name__ == "__main__":
    main()