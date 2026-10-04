from orthogonalization import orthogonalize, aug_orthogonalize
from matutil import coldict2mat
from vecutil import list2vec
from math import sqrt
def find_norm(vec):
    return sqrt(vec * vec)
def orthonormalize(vectors):
    orthogonal_vectors = orthogonalize(vectors)
    norms = [find_norm(vec) for vec in orthogonal_vectors]
    return [(1 / norm) * vec for vec, norm in zip(orthogonal_vectors, norms)]
def adjust(vector, multipliers):
    return Vec(vector.D, {i: vector[i] * multipliers[i] for i in vector.D})
def aug_orthonormalize(vectors):
    orthogonal_vectors, sigma_dict = aug_orthogonalize(vectors)
    norms = [find_norm(vec) for vec in orthogonal_vectors]
    R = [adjust(sigma, norms) for sigma in sigma_dict]
    Q = [(1 / norm) * vec for vec, norm in zip(orthogonal_vectors, norms)]
    return Q, R
if __name__ == "__main__":
    vectors1 = [list2vec(l) for l in [[6, 6], [2, 0]]]
    Q1, R1 = aug_orthonormalize(vectors1)
    Q_mat1 = coldict2mat(Q1)
    R_mat1 = coldict2mat(R1)
    print("Orthonormalized Vectors (Q):")
    print(Q_mat1)
    print("Adjustment Matrix (R):")
    print(R_mat1)
    print("Product of Q and R:")
    print(Q_mat1 * R_mat1)
    vectors2 = [list2vec(l) for l in [[2, 3], [2, 1], [1, 1]]]
    Q2, R2 = aug_orthonormalize(vectors2)
    Q_mat2 = coldict2mat(Q2)
    R_mat2 = coldict2mat(R2)
    print("Original Vectors:")
    print(coldict2mat(vectors2))
    print("Orthonormalized Vectors (Q):")
    print(Q_mat2)
    print("Adjustment Matrix (R):")
    print(R_mat2)
    print("Product of Q and R:")
    print(Q_mat2 * R_mat2)