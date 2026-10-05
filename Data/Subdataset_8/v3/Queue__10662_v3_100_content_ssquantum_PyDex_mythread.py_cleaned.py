import time
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication
class PyDexThread(QThread):
    stop_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.app = QApplication.instance()
        self.stop = False
        self.queue = []
    @pyqtSlot(object)
    def add_item(self, new_item):
        self.queue.append(new_item)
    def process(self, item):
        raise NotImplementedError
    def run(self):
        while True:
            self.app.processEvents()
            if self.check_stop():
                break
            elif self.queue:
                self.process(self.queue.pop(0))
            else:
                time.sleep(0.1)
    def check_stop(self):
        return self.stop
    def reset_stop(self):
        self.stop = False
    def close(self):
        self.stop_signal.emit()
        self.finished.disconnect(self.reset_stop)
        self.finished.connect(self.reset_stop)
def reset_slot(signal, slot, reconnect=True):
    while True:
        try:
            signal.disconnect(slot)
        except TypeError:
            break
    if reconnect:
        signal.connect(slot)