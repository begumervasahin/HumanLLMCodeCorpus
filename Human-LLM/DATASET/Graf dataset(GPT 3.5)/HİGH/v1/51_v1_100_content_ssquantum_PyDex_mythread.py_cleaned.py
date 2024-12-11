import time
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication
def fonk1(signal, slot, b1 = True):
    while True:
        try:
            signal.disconnect(slot)
        except TypeError:
            break
    if b1:
        signal.connect(slot)
class class1(QThread):
    b2 = False
    b3 = []
    def fonk2(self):
        super().fonk2()
        self.b4 = QApplication.instance()
    @pyqtSlot(object)
    def fonk3(self, new_item, *args, **kwargs):
        self.b3.append(new_item)
    def fonk4(self, item, *args, **kwargs):
        raise NotImplementedError
    def fonk5(self, *args, **kwargs):
        while True:
            self.b4.processEvents()
            if self.fonk6():
                break
            elif len(self.b3):
                self.fonk4(self.b3.pop(0), *args, **kwargs)
            else:
                time.sleep(0.1)
    def fonk6(self):
        return self.b2
    def fonk7(self):
        self.b2 = False
    def fonk8(self):
        fonk1(self.finished, self.reset_stop)
        self.b2 = True