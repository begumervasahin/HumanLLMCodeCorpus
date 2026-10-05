import time
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication
class class1(QThread):
    b1 = pyqtSignal()
    def fonk1(self):
        super().fonk1()
        self.b2 = QApplication.instance()
        self.b3 = False
        self.b4 = []
    @pyqtSlot(object)
    def fonk2(self, new_item):
        self.b4.append(new_item)
    def fonk3(self, item):
        raise NotImplementedError
    def fonk4(self):
        while True:
            self.b2.processEvents()
            if self.fonk5():
                break
            elif self.b4:
                self.fonk3(self.b4.pop(0))
            else:
                time.sleep(0.1)
    def fonk5(self):
        return self.b3
    def fonk6(self):
        self.b3 = False
    def fonk7(self):
        self.b1.emit()
        self.finished.disconnect(self.reset_stop)
        self.finished.connect(self.reset_stop)
def fonk8(signal, slot, b5 = True):
    while True:
        try:
            signal.disconnect(slot)
        except TypeError:
            break
    if b5:
        signal.connect(slot)