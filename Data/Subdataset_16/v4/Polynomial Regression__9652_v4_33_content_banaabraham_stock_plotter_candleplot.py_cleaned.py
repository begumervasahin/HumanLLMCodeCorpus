import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui
import urllib.request
import pandas as pd
import numpy as np
class class1(pg.GraphicsObject):
    def fonk1(self, b1):
        super().fonk1()
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
def fonk5(ticker):
    b5 = f"https:
    b6 = f"{ticker}.csv"
    urllib.request.urlretrieve(b5, b6)
    b1 = pd.read_csv(b6)
    b1 = b1.iloc[::-1]
    b7 = np.arange(1, len(b1) + 1)
    b1.drop(['Date', 'Volume'], b8 = 1, inplace=True)
    b9 = [
        (b7[i], b1['Open'][i], b1['Close'][i], b1['Low'][i], b1['High'][i])
        for i in range(len(b1))
    ]
    return b9
if b10 = = '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        b11 = QtGui.QApplication([])
        b12 = [
            (1., 10, 13, 5, 15),
            (2., 13, 17, 9, 20),
            (3., 17, 14, 11, 23),
            (4., 14, 15, 5, 19),
            (5., 15, 9, 8, 22),
            (6., 9, 15, 8, 16),
        ]
        b13 = class1(b12)
        b14 = pg.b14()
        b14.addItem(b13)
        b14.setWindowTitle('PyQtGraph Example: Custom Candlestick Item')
        QtGui.QApplication.instance().exec_()