from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication
b1 = 'mbcs'
class class1(QThread):
    b2 = pyqtSignal()
    def fonk1(self):
        super().fonk1()
        self.b3 = QApplication.instance()
        self.b4 = []
    @pyqtSlot(object)
    def fonk2(self, new_item, *args, **kwargs):
        self.b4.append(new_item)
    def fonk3(self, item, *args, **kwargs):
        raise NotImplementedError
    def fonk4(self, *args, **kwargs):
        while True:
            self.b3.processEvents()
            if self.fonk5():
                break
            elif self.b4:
                self.fonk3(self.b4.pop(0), *args, **kwargs)
    def fonk5(self):
        return self.b2
    def fonk6(self):
        self.b2 = False
    def fonk7(self):
        self.b2.emit()
        self.b2.connect(self.reset_stop)
def fonk8(signal, slot, b5 = True):
    while True:
        try:
            signal.disconnect(slot)
        except TypeError:
            break
    if b5:
        signal.connect(slot)