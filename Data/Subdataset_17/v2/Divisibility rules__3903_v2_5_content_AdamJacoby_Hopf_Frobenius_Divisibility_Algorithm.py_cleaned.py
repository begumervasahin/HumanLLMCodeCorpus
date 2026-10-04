import sympy as sp
import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as sps_linalg
from itertools import product
from math import floor
from HopfConstructions_Functions import Tensor_Mult, Left_Action_Matrix
from Frobenius_Tools import Compute_M, CharPoly, Multiplicity, HigmanTrace, Remove_Zeros_At_Zero
from Algebra_Tools import Center, AlgebraElement
def compute_central_matrix(A):
    M = np.array(Compute_M(A).toarray())
    U, UI, center_dim = Center(A)
    M = UI.dot(M.dot(U))
    M = np.array(M.tolist())
    M = M[0:center_dim, 0:center_dim]
    print(M.shape)
    return M
def check_finite_dimensional(A):
    dim = A.dim
    if A.casimir_flag == 'no':
        A.GetCasimir()
    mult = A.mult
    casimir = A.casimir
    tensor_mult = Tensor_Mult(A, A)
    C = mult.dot(tensor_mult.dot(np.kron(casimir, casimir)))
    C = AlgebraElement(C, A)
    temp = C**2 - (dim**2) * C
    divisors = sp.divisors(dim**2)
    for d in divisors[1:]:
        temp = temp * C**2 - (dim**2 / d) * C
    zeros = np.zeros(dim)
    if np.array_equal(temp.vector, zeros):
        print('Yes FD')
    else:
        print('No FD')
def degree_of_irreps_char(A):
    dim = A.dim
    number_of_irreps = []
    sizes_of_irreps = []
    M = Compute_M(A)
    poly = CharPoly(M)
    Der = [poly]
    d = dim
    bound = floor(dim**0.5)
    i = 1
    while i <= bound:
        root_to_test = dim**2 / i**2
        if poly.eval(root_to_test) == 0:
            sizes_of_irreps.append(i)
            temp = Multiplicity(poly, root_to_test, Der)
            number_of_irreps.append(temp[0] / i**2)
            d -= temp[0]
            Der = temp[1]
            bound = floor(d**0.5)
        i += 1
    return [sizes_of_irreps, number_of_irreps]
def degree_of_irreps_higchar(A):
    dim = A.dim
    number_of_irreps = []
    sizes_of_irreps = []
    M = Compute_M(A)
    higman_trace = HigmanTrace(A) / dim
    M = M.dot(higman_trace)
    poly = CharPoly(M)
    poly = Remove_Zeros_At_Zero(poly)
    print(poly)
    Der = [poly]
    d = dim
    bound = floor(dim**0.5)
    i = 1
    while i <= bound:
        root_to_test = dim**2 / i**2
        if poly.eval(root_to_test) == 0:
            sizes_of_irreps.append(i)
            temp = Multiplicity(poly, root_to_test, Der)
            number_of_irreps.append(temp[0])
            d -= temp[0]
            Der = temp[1]
            bound = floor(d**0.5)
        i += 1
    return [sizes_of_irreps, number_of_irreps]
def degree_of_irreps_det(A):
    dim = A.dim
    sizes_of_irreps = []
    M = Compute_M(A)
    M = np.array(M.toarray())
    d = dim
    float_dim = float(dim)
    bound = floor(dim**0.5)
    root_dim = bound
    i = 1
    while i <= bound:
        n = float(i)
        value_to_test = float_dim**2 / n**2
        if i == root_dim:
            error = ((float_dim**2 * (2 * n - 1) / (n**2 * (n - 1)**2))**float_dim) / 2
        else:
            error = ((float_dim**2 * (2 * n + 1) / (n**2 * (n + 1)**2))**float_dim) / 2
        if np.linalg.det(M - value_to_test * np.identity(dim)) < error:
            sizes_of_irreps.append(i)
            d -= i**2
            bound = floor(d**0.5)
        i += 1
    return sizes_of_irreps
def degree_of_irreps_eig(A):
    dim = A.dim
    M = Compute_M(A)
    M = np.array(M.toarray())
    temp = np.round(np.sqrt(dim**2 / np.real(np.linalg.eigvals(M)))).tolist()
    eigen_vals = sorted(list(set(temp)))
    multiplicities = [temp.count(val) / val**2 for val in eigen_vals]
    print(f'The dimensions of the irreps: {eigen_vals}')
    print(f'With corresponding multiplicities: {multiplicities}')
def degree_of_irreps_center(A):
    dim = A.dim
    M = compute_central_matrix(A)
    temp = np.round(np.sqrt(dim**2 / np.real(np.linalg.eigvals(M)))).tolist()
    eigen_vals = sorted(list(set(temp)))
    multiplicities = [temp.count(val) for val in eigen_vals]
    print(f'The dimensions of the irreps: {eigen_vals}')
    print(f'With corresponding multiplicities: {multiplicities}')
if __name__ == "__main__":
    pass