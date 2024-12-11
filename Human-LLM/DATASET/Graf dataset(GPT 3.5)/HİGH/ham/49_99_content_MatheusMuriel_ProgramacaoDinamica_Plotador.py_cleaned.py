import matplotlib
import matplotlib.pyplot as plt
import numpy as np
def fonk1(b10, b11, b12):
  b1 = np.array(b10)
  b2 = np.array(b11)
  fig, b3 = plt.subplots()
  b3.plot(b1, b2)
  b3.set(b4 = 'Tamanho N', ylabel='Tempo de execuÃ§Ã£o',
        b5 = b12)
  b3.grid()
  plt.show()
def fonk2(inicio, fim, y1, label1, y2, label2):
  b6 = np.array(y1)
  b7 = np.array(y2)
  a1 = 0
  b8 = max(y1)
  b9 = max(y2)
  a1 = b8 if b8 > b9 else b9
  b10 = range(inicio, fim+1)
  b11 = range(0, int(float(a1))+1)
  fig, b3 = plt.subplots()
  b3.plot(b10, b6, b12 = label1)
  b3.plot(b10, b7, b12 = label2)
  b3.set(b4 = 'Tamanho N', ylabel='Tempo de execuÃ§Ã£o',
        b5 = "{} b10 {}".format(label1, label2))
  plt.legend()
  plt.show()