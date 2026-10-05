import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')
class FibonacciScatter(object):
    def FibonacciSequence(self, length):
        p1, p2 = 0, 1
        fibList = []
        for each in range(length):
            fibList.append(p1)
            p1,p2 = p2, p1+p2
        return fibList
    def ScatterSequence(self, seq):
        x = []
        y = []
        for position, value in enumerate(seq):
           x.append(position)
           y.append(value)
        plt.scatter(x,y)
        plt.show()
if __name__ == "__main__":
    x = FibonacciScatter()
    data = x.FibonacciSequence(10)
    x.ScatterSequence(data)