
import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui
import urllib
import pandas as pd
import numpy as np
class class1(pg.GraphicsObject):
    def fonk1(self, b1):
        pg.GraphicsObject.fonk1(self)
        self.b1 = b1
        self.fonk2()
    def fonk2(self):
        self.b2 = QtGui.QPicture()
        b3 = QtGui.QPainter(self.b2)
        b3.setPen(pg.mkPen('b4'))
        b4 = (self.b1[1][0] - self.b1[0][0]) / 3.
        for (t, open, close, min, max) in self.b1:
            b3.drawLine(QtCore.QPointF(t, min), QtCore.QPointF(t, max))
            if open > close:
                b3.setBrush(pg.mkBrush('r'))
            else:
                b3.setBrush(pg.mkBrush('g'))
            b3.drawRect(QtCore.QRectF(t-b4, open, b4*2, close-open))
        b3.end()
    def fonk3(self, b3, *args):
        b3.drawPicture(0, 0, self.b2)
    def fonk4(self):
        return QtCore.QRectF(self.b2.fonk4())
"""
b5 = 'aapl'
b6 = "https:
b7 = b5+".csv"
urllib.request.urlretrieve(b6,b7)
b8 = pd.read_csv(b7)
b8.iloc[:] = b8.iloc[::-1].values
b9 = np.arange(1,len(b8)+1,1.0)
del b8['Date']
del b8['Volume']
b1 = []
for i in range(len(b8)):
    b10 = (b9[i], b8['Open'][i], b8['Close'][i], b8['Low'][i], b8['High'][i])
    b10 = tuple(b10)
    b1.append(b10)
b11 = [
    (1., 10, 13, 5, 15),
    (2., 13, 17, 9, 20),
    (3., 17, 14, 11, 23),
    (4., 14, 15, 5, 19),
    (5., 15, 9, 8, 22),
    (6., 9, 15, 8, 16),
]
b12 = class1(b1)
b13 = pg.plot()
b13.addItem(b12)
b13.setWindowTitle('pyqtgraph example: customGraphicsItem')
"""
if b14 = = '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()