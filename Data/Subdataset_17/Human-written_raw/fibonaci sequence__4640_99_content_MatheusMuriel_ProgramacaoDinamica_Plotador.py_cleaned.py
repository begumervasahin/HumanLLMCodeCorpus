import matplotlib
import matplotlib.pyplot as plt
import numpy as np
def plot_simples(x, y, label):
  xx = np.array(x)
  yy = np.array(y)
  fig, ax = plt.subplots()
  ax.plot(xx, yy)
  ax.set(xlabel='Tamanho N', ylabel='Tempo de execuÃ§Ã£o',
        title=label)
  ax.grid()
  plt.show()
def plot_duplo(inicio, fim, y1, label1, y2, label2):
  yy1 = np.array(y1)
  yy2 = np.array(y2)
  max_time = 0
  max_time_y1 = max(y1)
  max_time_y2 = max(y2)
  max_time = max_time_y1 if max_time_y1 > max_time_y2 else max_time_y2
  x = range(inicio, fim+1)
  y = range(0, int(float(max_time))+1)
  fig, ax = plt.subplots()
  ax.plot(x, yy1, label=label1)
  ax.plot(x, yy2, label=label2)
  ax.set(xlabel='Tamanho N', ylabel='Tempo de execuÃ§Ã£o',
        title="{} x {}".format(label1, label2))
  plt.legend()
  plt.show()