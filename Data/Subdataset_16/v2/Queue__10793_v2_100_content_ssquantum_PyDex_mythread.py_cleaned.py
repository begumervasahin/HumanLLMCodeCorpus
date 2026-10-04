
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
    def fonk3(self, new_item):
        self.b3.append(new_item)
    def fonk4(self, item):
        raise NotImplementedError("Subclasses should implement this method")
    def fonk5(self):
        while True:
            self.b4.processEvents()
            if self.fonk6():
                break
            elif self.b3:
                self.fonk9(self.b3.pop(0))
    def fonk6(self):
        return self.b2
    def fonk7(self):
        self.b2 = False
    def fonk8(self):
        fonk1(self.finished, self.reset_stop)
        self.b2 = True
class class2(class1):
    def fonk9(self, item):
        print(f"Processing item: {item}")
def fonk10():
    import sys
    import time
    b4 = QApplication(sys.argv)
    b5 = class2()
    b5.start()
    b5.fonk3("Item 1")
    b5.fonk3("Item 2")
    time.sleep(5)
    b5.fonk8()
    b5.wait()
    print("Thread stopped.")
if b6 = = "__main__":
    fonk10()