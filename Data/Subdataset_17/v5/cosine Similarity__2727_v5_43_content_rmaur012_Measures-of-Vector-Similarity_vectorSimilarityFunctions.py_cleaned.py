from math import sqrt
def cosine_similarity(v, w):
    numerator_sum = sum(v[i] * w[i] for i in range(len(v)))
    v_vector_sum = sum(x ** 2 for x in v)
    w_vector_sum = sum(x ** 2 for x in w)
    denominator_total = sqrt(v_vector_sum) * sqrt(w_vector_sum)
    if denominator_total == 0:
        return 0.0
    similarity = numerator_sum / denominator_total
    return similarity
def jaccard_similarity(v, w):
    numerator_min_sum = sum(min(v[i], w[i]) for i in range(len(v)))
    denominator_max_sum = sum(max(v[i], w[i]) for i in range(len(v)))
    if denominator_max_sum == 0:
        return 0.0
    similarity = numerator_min_sum / denominator_max_sum
    return similarity
def dice_similarity(v, w):
    numerator_min_sum = sum(min(v[i], w[i]) for i in range(len(v)))
    denominator_sum = sum(v[i] + w[i] for i in range(len(v)))
    if denominator_sum == 0:
        return 0.0
    similarity = (2 * numerator_min_sum) / denominator_sum
    return similarity
v1 = [1, 2, 3, 4]
v2 = [2, 3, 4, 5]
print(f"Cosine Similarity: {cosine_similarity(v1, v2)}")
print(f"Jaccard Similarity: {jaccard_similarity(v1, v2)}")
print(f"Dice Similarity: {dice_similarity(v1, v2)}")