import pandas
import numpy
b1 = False
b2 = "irisTraining.txt"
b3 = pandas.read_csv(b2, sep=" ", header=None)
b4 = "irisTesting.txt"
b5 = pandas.read_csv(b4, sep=" ", header=None)
b6 = []
b7 = b5.shape[1]
for i in range(b7 - 1):
  b6.append(i)
b6.append("label")
b3.b8 = b6
b5.b8 = b6
b9 = b3.shape[0]
b10 = b5.shape[0]
b11 = b3[b3['label'] == 1].shape[0]
b12 = b3[b3['label'] == -1].shape[0]
b13 = b5['label']
del b5['label']
a1 = 0
a2 = 0
a3 = 0
a4 = 0
def fonk1(x, m, s):
  return (1/(2 * numpy.pi * s**2)**0.5) * numpy.exp(-1 * (x-m)**2 / (2 * s**2))
b14 = b5.shape[0]
for i in range(b14):
  b15 = b5.iloc[i]
  a5 = 1
  a6 = 1
  for attribute, value in b15.iteritems():
    b16 = numpy.array(b3[b3['label'] == 1][attribute])
    b17 = numpy.average(b16)
    b18 = numpy.std(b16)
    b19 = numpy.array(b3[b3['label'] == -1][attribute])
    b20 = numpy.average(b19)
    b21 = numpy.std(b19)
    a5 *= fonk1(value, b17, b18)
    a6 *= fonk1(value, b20, b21)
  a5 = a5 * b11
  a6 = a6 * b12
  b22 = 1 if a5 > a6 else -1
  b23 = b13.values[i]
  if (b22 = = 1):
    if (b23 = = 1):
      a1 += 1
    else:
      a3 += 1
  elif b22 = = -1:
    if (b23 = = -1):
      a2 += 1
    else:
      a4 += 1
print('--- ---')
print('counts')
print('a1')
print(a1)
print('a2')
print(a2)
print('a3')
print(a3)
print('a4')
print(a4)
b24 = (a1 + a2) / b10
print('b24: ', b24)
b25 = a1 / (a1 + a4)
print('b25 / recall: ', b25)
b26 = a2 / (a3 + a2)
print('b26: ', b26)
b27 = a1 / (a1 + a3)
print('b27: ', b27)