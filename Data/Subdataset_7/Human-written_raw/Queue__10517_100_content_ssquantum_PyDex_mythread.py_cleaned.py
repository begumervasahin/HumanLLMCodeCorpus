
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication
b1 = 'mbcs'
def fonk1(signal, slot, b2 = True):
    while True:
        try: signal.disconnect(slot)
        except TypeError: break
    if b2: signal.connect(slot)
class class1(QThread):
    b3 = False
    b4 = []
    def fonk2(self):
        super().fonk2()
        self.b5 = QApplication.instance()
    @pyqtSlot(object)
    def fonk3(self, new_item, *args, **kwargs):
        self.b4.append(new_item)
    def fonk4(self, item, *args, **kwargs):
        raise NotImplementedError
    def fonk5(self, *args, **kwargs):
        while True:
            self.b5.processEvents()
            if self.fonk6():
                break
            elif len(self.b4):
                self.fonk4(self.b4.pop(0), *args, **kwargs)
    def fonk6(self):
        return self.b3
    def fonk7(self):
        self.b3 = False
    def fonk8(self):
        fonk1(self.finished, self.reset_stop)
        self.b3 = True