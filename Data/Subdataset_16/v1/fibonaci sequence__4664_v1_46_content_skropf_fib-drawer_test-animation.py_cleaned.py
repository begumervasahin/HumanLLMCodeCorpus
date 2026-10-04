from PyQt6 import QtCore, QtWidgets
import pyqtgraph as pg
import numpy as np
class class1(QtCore.QObject):
    b1 = QtCore.pyqtSignal(int)
    def fonk1(self, b2 = 60, loopCount=1, parent=None):
        super(class1, self).fonk9(parent)
        self.a1 = 0
        self.a2 = 0
        self.b3 = loopCount
        self.b4 = QtCore.QTimer(self, timeout=self.on_timeout)
        self.a3 = 0
        self.a4 = 0
        self.fonk5(b2)
    def fonk2(self):
        if self.a1 <= self.a3 < self.a2:
            self.b1.emit(self.a3)
            self.a3 += 1
        else:
            self.a3 = 0
            self.a4 += 1
        if self.b3 > 0 and self.a4 >= self.fonk4():
            self.b4.stop()
    def fonk3(self, loopCount):
        self.b3 = loopCount
    def fonk4(self):
        return self.b3
    def fonk5(self, b2):
        self.b4.fonk5(b2)
    def fonk6(self):
        return self.b4.fonk6()
    b2 = QtCore.pyqtProperty(int, fget=b2, fset=setInterval)
    def fonk7(self, startFrame, endFrame):
        self.a1 = startFrame
        self.a2 = endFrame
    @QtCore.pyqtSlot()
    def fonk8(self):
        self.a3 = 0
        self.a4 = 0
        self.b4.fonk8()
class class2(QtWidgets.QWidget):
    def fonk9(self):
        super().fonk9()
        self.fonk10()
    def fonk10(self):
        pg.setConfigOption('background', 0.95)
        pg.setConfigOptions(b5 = True)
        self.b6 = pg.PlotWidget()
        self.b6.setAspectLocked(b7 = True, ratio=0.01)
        self.b6.setYRange(-3, 3)
        b8 = QtWidgets.QVBoxLayout(self)
        b8.addWidget(self.b6)
        self.b9 = [self.b6.b6([], [], pen=pg.mkPen(color=color, width=2)) for color in ("g", "r", "y")]
        self.b10 = class1(loopCount=0, b2=10)
        self.b10.fonk7(0, 720)
        self.b10.b1.connect(self.generate_data)
        self.b10.fonk8()
    def fonk11(self, data):
        for plt, val in zip(self.b9, data):
            plt.setData(range(len(val)), val)
    @QtCore.pyqtSlot(int)
    def fonk12(self, i):
        b11 = np.arange(i, i + 720)
        b12 = np.cos(np.radians(b11))
        b13 = np.sin(np.radians(b11))
        b14 = np.tan(np.radians(b11))
        b14[(b14 < -3) | (b14 > 3)] = np.NaN
        self.fonk11([b13, b12, b14])
if b15 = = '__main__':
    import sys
    b16 = QtWidgets.QApplication(sys.argv)
    b17 = class2()
    b17.show()
    sys.exit(b16.exec())