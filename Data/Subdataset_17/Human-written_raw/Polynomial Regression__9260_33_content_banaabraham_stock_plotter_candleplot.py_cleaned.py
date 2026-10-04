
import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui
import urllib
import pandas as pd
import numpy as np
class CandlestickItem(pg.GraphicsObject):
    def __init__(self, data):
        pg.GraphicsObject.__init__(self)
        self.data = data
        self.generatePicture()
    def generatePicture(self):
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('w'))
        w = (self.data[1][0] - self.data[0][0]) / 3.
        for (t, open, close, min, max) in self.data:
            p.drawLine(QtCore.QPointF(t, min), QtCore.QPointF(t, max))
            if open > close:
                p.setBrush(pg.mkBrush('r'))
            else:
                p.setBrush(pg.mkBrush('g'))
            p.drawRect(QtCore.QRectF(t-w, open, w*2, close-open))
        p.end()
    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)
    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())
"""
ticker='aapl'
url="https:
stock=ticker+".csv"
urllib.request.urlretrieve(url,stock)
d=pd.read_csv(stock)
d.iloc[:] = d.iloc[::-1].values
x=np.arange(1,len(d)+1,1.0)
del d['Date']
del d['Volume']
data=[]
for i in range(len(d)):
    temp=(x[i], d['Open'][i], d['Close'][i], d['Low'][i], d['High'][i])
    temp=tuple(temp)
    data.append(temp)
dat = [
    (1., 10, 13, 5, 15),
    (2., 13, 17, 9, 20),
    (3., 17, 14, 11, 23),
    (4., 14, 15, 5, 19),
    (5., 15, 9, 8, 22),
    (6., 9, 15, 8, 16),
]
item = CandlestickItem(data)
plt = pg.plot()
plt.addItem(item)
plt.setWindowTitle('pyqtgraph example: customGraphicsItem')
"""
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()