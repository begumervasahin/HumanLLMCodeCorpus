class Vec:
    def __init__(self, domain, function):
        self.D = domain
        self.f = function
    def __repr__(self):
        return f"Vec({self.D},{self.f})"
    def __getitem__(self, key):
        return self.f.get(key, 0)
    def __setitem__(self, key, value):
        self.f[key] = value
from vec import Vec
def list2vec(L):
    return Vec(set(range(len(L))), {k: L[k] for k in range(len(L))})
def zero_vec(D):
    return Vec(D, {d: 0 for d in D})
from functions import list2vec, zero_vec
from vec import Vec
def main():
    vec1 = list2vec([10, 20, 30])
    print(vec1)
    vec2 = zero_vec({0, 1, 2, 3})
    print(vec2)
if __name__ == "__main__":
    main()