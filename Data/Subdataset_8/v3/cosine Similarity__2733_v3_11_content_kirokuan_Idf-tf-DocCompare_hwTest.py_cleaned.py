from __future__ import division
import unittest
def calculate_jaccard_similarity(list1, list2):
    intersection = len(set(list1).intersection(set(list2)))
    union = len(set(list1).union(set(list2)))
    return intersection / union if union != 0 else 0
def calculate_idf(matrix):
    num_docs = len(matrix)
    idf = []
    for col in range(len(matrix[0])):
        count = sum([1 for row in matrix if row[col] > 0])
        idf_val = 0 if count == 0 else num_docs / count
        idf.append(idf_val)
    return idf
def create_dummy_idf(matrix):
    return [1 if any(row) else 0 for row in zip(*matrix)]
def calculate_tf(keys, freqs):
    total_freq = sum(freqs.values())
    tf_list = [freqs.get(key, 0) / total_freq for key in keys]
    return tf_list
def provide_feedback(query, doc_vectors, key_position):
    doc_keys = list(doc_vectors.keys())
    feedback_scores = []
    for key in doc_keys:
        doc_vector = doc_vectors[key]
        score = sum([query[i] * doc_vector[key_position[key]] for i in range(len(query))])
        feedback_scores.append(score)
    return feedback_scores
class TestHwMethods(unittest.TestCase):
    def test_jaccard_similarity(self):
        self.assertEqual(calculate_jaccard_similarity([1, 2, 0, 1], [0, 0, 1, 1]), 0.25)
    def test_idf_calculation(self):
        self.assertEqual(calculate_idf([[0.5, 0, 0, 0.2], [0.2, 0.01, 0.5, 1], [0.2, 0.4, 0, 1]]),
                         [0.0, 0.17609125905568124, 0.47712125471966244, 0.0])
    def test_dummy_idf_creation(self):
        self.assertEqual(create_dummy_idf([[0, 0, 0, 1], [0, 0, 1, 1], [1, 1, 0, 1]]), [1, 1, 1, 1])
    def test_tf_calculation(self):
        freq = {"this": 3, "that": 5}
        key = {"this": 0, "that": 1, "test": 2}
        self.assertEqual(calculate_tf(key, freq), [3 / 8, 5 / 8, 0])
    def test_feedback_scores(self):
        doc_vectors = {"test1": [10] * 25}
        key_position = {'2for': 0, 'ar': 1, 'motor': 2, 'carbon': 3, 'sharp': 4}
        query = [1] * 25
        result = [1.0, 1.0, 0.0, 0.0, 0.0]
        real_result = provide_feedback(query, doc_vectors, key_position)
        self.assertEqual(real_result, result)
        self.assertEqual(real_result.count(6), 0)
    def test_feedback_scores2(self):
        doc_vectors = {"test1": [10] * 52}
        key_position = {'clip': 0, '18-volt,': 1, '2for': 3, 'hook': 4, 'ar': 5, 'motor': 6}
        query = [1] * 52
        real_result = provide_feedback(query, doc_vectors, key_position)
        self.assertEqual(real_result.count(6), 0)
if __name__ == '__main__':
    unittest.main()