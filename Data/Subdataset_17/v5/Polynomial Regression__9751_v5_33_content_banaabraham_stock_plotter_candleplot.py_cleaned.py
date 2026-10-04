import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui
import urllib.request
import pandas as pd
import numpy as np
class CandlestickItem(pg.GraphicsObject):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.generate_picture()
    def generate_picture(self):
        self.picture = QtGui.QPicture()
        painter = QtGui.QPainter(self.picture)
        painter.setPen(pg.mkPen('w'))
        w = (self.data[1][0] - self.data[0][0]) / 3.0
        for (t, open, close, low, high) in self.data:
            painter.drawLine(QtCore.QPointF(t, low), QtCore.QPointF(t, high))
            color = 'r' if open > close else 'g'
            painter.setBrush(pg.mkBrush(color))
            painter.drawRect(QtCore.QRectF(t-w, open, w*2, close-open))
        painter.end()
    def paint(self, painter, *args):
        painter.drawPicture(0, 0, self.picture)
    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())
def download_stock_data(ticker):
    url = f"https:
    stock_file = f"{ticker}.csv"
    urllib.request.urlretrieve(url, stock_file)
    return pd.read_csv(stock_file)
def prepare_stock_data(ticker):
    data = download_stock_data(ticker)
    data = data.iloc[::-1]
    x = np.arange(1, len(data) + 1)
    data.drop(columns=['Date', 'Volume'], inplace=True)
    processed_data = [
        (x[i], data['Open'][i], data['Close'][i], data['Low'][i], data['High'][i])
        for i in range(len(data))
    ]
    return processed_data
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        app = QtGui.QApplication([])
        example_data = [
            (1., 10, 13, 5, 15),
            (2., 13, 17, 9, 20),
            (3., 17, 14, 11, 23),
            (4., 14, 15, 5, 19),
            (5., 15, 9, 8, 22),
            (6., 9, 15, 8, 16),
        ]
        item = CandlestickItem(example_data)
        plot = pg.plot()
        plot.addItem(item)
        plot.setWindowTitle('PyQtGraph Example: Custom Candlestick Item')
        QtGui.QApplication.instance().exec_()