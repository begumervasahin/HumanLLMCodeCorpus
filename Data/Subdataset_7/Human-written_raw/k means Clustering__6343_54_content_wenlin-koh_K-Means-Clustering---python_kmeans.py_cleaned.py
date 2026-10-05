import math
import numpy as np
def fonk1(filename: str) -> np.array:
  """
  Brief :
    Opens file "filename" and load dataset from file and b1 as an array
  Parameters :
    filename : Name of the file.
  Returns :
    An array containing dataset in the file.
  """
  b1 = []
  b2 = open(filename, "r")
  b3 = b2.readlines()
  a1 = 0
  for line in b3:
    b1.append([])
    b4 = line.split('\t')
    for word in b4:
      b1[a1].append(float(word))
    b1[a1].append(0)
    a1 = a1 + 1
  b2.close()
  return np.asarray(b1)
def fonk2(X: np.array, M: np.array):
  a2 = 0.0
  for x in X:
    print(np.linalg.norm(x[:-1] - M[int(x[-1])]))
    a2 = a2 + np.linalg.norm(x[:-1] - M[int(x[-1])])
  return (1.0 / X.shape[0]) * a2
def fonk3(X: np.array, M: np.array):
  b5 = np.zeros(M.shape)
  b6 = [0 for i in range(M.shape[0])]
  for x in X:
    b7 = int(x[-1])
    b5[b7] += x[:-1]
    b6[b7] += 1
  for i in range(M.shape[0]):
    b5[i] = b5[i] / b6[i]
  return b5
def fonk4(X: np.array, M: np.array):
  for i in range(X.shape[0]):
    b8 = np.asarray([n for n in X[i][:-1]])
    b9 = float("inf")
    b7 = 0
    for c in M:
      b10 = np.linalg.norm(b8 - c)
      if b10 < b9:
        b9 = b10
        X[i][-1] = b7
      b7 = b7 + 1
  return X