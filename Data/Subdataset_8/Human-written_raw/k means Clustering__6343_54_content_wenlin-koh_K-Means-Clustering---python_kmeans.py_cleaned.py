import math
import numpy as np
def loadData(filename: str) -> np.array:
  """
  Brief :
    Opens file "filename" and load dataset from file and output as an array
  Parameters :
    filename : Name of the file.
  Returns :
    An array containing dataset in the file.
  """
  output = []
  dataFile = open(filename, "r")
  lines = dataFile.readlines()
  id = 0
  for line in lines:
    output.append([])
    words = line.split('\t')
    for word in words:
      output[id].append(float(word))
    output[id].append(0)
    id = id + 1
  dataFile.close()
  return np.asarray(output)
def errCompute(X: np.array, M: np.array):
  error = 0.0
  for x in X:
    print(np.linalg.norm(x[:-1] - M[int(x[-1])]))
    error = error + np.linalg.norm(x[:-1] - M[int(x[-1])])
  return (1.0 / X.shape[0]) * error
def calcMean(X: np.array, M: np.array):
  newM = np.zeros(M.shape)
  counter = [0 for i in range(M.shape[0])]
  for x in X:
    cid = int(x[-1])
    newM[cid] += x[:-1]
    counter[cid] += 1
  for i in range(M.shape[0]):
    newM[i] = newM[i] / counter[i]
  return newM
def Group(X: np.array, M: np.array):
  for i in range(X.shape[0]):
    p = np.asarray([n for n in X[i][:-1]])
    shortest = float("inf")
    cid = 0
    for c in M:
      dist = np.linalg.norm(p - c)
      if dist < shortest:
        shortest = dist
        X[i][-1] = cid
      cid = cid + 1
  return X